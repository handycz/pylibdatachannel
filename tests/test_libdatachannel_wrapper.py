import concurrent.futures
import queue
import threading

import pytest
from pylibdatachannel import Candidate, Configuration, DataChannel, Description, DescriptionType, IceServer, IceServerRelayType, PeerConnection, State


def test_create_ice_server():
    server = IceServer("stun:example.com", 1234)
    assert server.username == ""
    assert server.password == ""
    assert server.hostname == "stun:example.com"
    assert server.port == 1234

    server_with_credentials = IceServer("stun:example.com", 1234, "ozobot", "secretpassword", IceServerRelayType.TURN_UDP)
    assert server_with_credentials.username == "ozobot"
    assert server_with_credentials.password == "secretpassword"
    assert server_with_credentials.hostname == "stun:example.com"
    assert server_with_credentials.port == 1234
    assert server_with_credentials.relay_type == IceServerRelayType.TURN_UDP


def test_configuration():
    configuration = Configuration(
        [
            IceServer("stun:example.com", 1234),
        ]
    )

    assert configuration.ice_servers[0].hostname == "stun:example.com"
    assert configuration.ice_servers[0].port == 1234
    assert len(configuration.ice_servers) == 1


def test_candidate():
    with pytest.raises(ValueError):
        _ = Candidate("xxx", "yyy")

    candidate = Candidate("candidate:5 1 UDP 92150271 216.39.253.22 45840 typ relay raddr 216.39.253.22 rport 45840", "0")
    assert candidate.candidate == "a=candidate:5 1 UDP 92150271 216.39.253.22 45840 typ relay raddr 216.39.253.22 rport 45840"
    assert candidate.mid == "0"


def test_description():
    description_str = (
        "v=0\r\no=- 3936842077 0 IN IP4 127.0.0.1\r\ns=-\r\nt=0 0\r\na=setup:actpass\r\n"
        "m=application 9 UDP/DTLS/SCTP webrtc-datachannel\r\nc=IN IP4 0.0.0.0\r\na=mid:0\r\na=sendrecv\r\na=sctp-port:5000\r\n"
        "a=max-message-size:65536\r\na=candidate:9046f6b83f321e7124cad4d4dc60b110 1 udp 2130706431 10.79.80.241 43970 typ host\r\n"
        "a=candidate:bad3700ba3bd29fee2797c8e0bb8215a 1 udp 2130706431 2a03:a900:2020:a3:da3a:ddff:fe04:8127 41454 typ host\r\n"
        "a=candidate:4c51db84f96d241102c7e687b1077e5d 1 udp 1694498815 88.146.116.167 43970 typ srflx raddr 10.79.80.241 rport 43970\r\n"
        "a=candidate:bf46076bc5b044080f7d76470e336d40 1 udp 16777215 216.39.253.22 39098 typ relay raddr 10.79.80.241 rport 46866\r\n"
        "a=end-of-candidates\r\n"
    )

    desc = Description(f'{{"sdp": "{description_str}"}}', DescriptionType.ANSWER)
    assert desc.type == DescriptionType.ANSWER


def test_peer_connection_initialization():
    configuration = Configuration(
        [
            IceServer("stun:example.com", 1234),
        ]
    )

    _ = PeerConnection(configuration=configuration)
    _ = PeerConnection()


def _create_peer_connections() -> tuple[PeerConnection, PeerConnection]:
    pc1 = PeerConnection()
    pc2 = PeerConnection()

    pc1.on_local_candidate(lambda cand: pc2.add_remote_candidate(cand))
    pc2.on_local_candidate(lambda cand: pc1.add_remote_candidate(cand))

    pc1.on_local_description(lambda desc: pc2.set_remote_description(desc))
    pc2.on_local_description(lambda desc: pc1.set_remote_description(desc))

    return pc1, pc2


def test_peer_connection_open_connection():
    pc1, pc2 = _create_peer_connections()

    pc1_connected_evt = threading.Event()
    pc2_connected_evt = threading.Event()

    pc1.on_state_change(lambda state: state == State.CONNECTED and pc1_connected_evt.set())
    pc2.on_state_change(lambda state: state == State.CONNECTED and pc2_connected_evt.set())

    _ = pc1.create_data_channel("test")

    pc1_connected_evt.wait(timeout=2)
    pc2_connected_evt.wait(timeout=2)

    assert pc1.state == State.CONNECTED
    assert pc2.state == State.CONNECTED


def test_peer_connection_open_channel():
    pc1, pc2 = _create_peer_connections()

    pc1_channel_open_evt = threading.Event()
    pc2_channel_fut = concurrent.futures.Future()

    pc2.on_data_channel(lambda channel: channel.label == "test" and pc2_channel_fut.set_result(channel))

    pc1_dc = pc1.create_data_channel("test")
    pc1_dc.on_open(pc1_channel_open_evt.set)

    pc1_channel_open_evt.wait(timeout=2)
    pc2_dc = pc2_channel_fut.result(timeout=2)

    assert pc1_dc.is_open
    assert pc1_dc.label == "test"

    assert pc2_dc.is_open
    assert pc2_dc.label == "test"


def test_peer_connection_send_message():
    pc1, pc2 = _create_peer_connections()

    pc1_dc_open_evt = threading.Event()
    message_queue = queue.Queue()

    def _on_channel(channel: DataChannel):
        def _on_open():
            channel.send("hello as string")
            channel.send(b"hello as binary")

            for i in range(3):
                channel.send(f"1->2: {i}")

        channel.on_open(_on_open)

    def _on_message(msg: str | bytes):
        message_queue.put(msg)

    pc2.on_data_channel(_on_channel)

    pc1_dc = pc1.create_data_channel("test")
    pc1_dc.on_open(pc1_dc_open_evt.set)
    pc1_dc.on_message(_on_message)

    pc1_dc_open_evt.wait(timeout=2)
    assert pc1_dc.is_open
    assert pc1.state == State.CONNECTED
    assert pc2.state == State.CONNECTED

    assert message_queue.get(timeout=2) == "hello as string"
    assert message_queue.get(timeout=2) == b"hello as binary"

    for i in range(3):
        assert message_queue.get(timeout=2) == f"1->2: {i}"


@pytest.mark.parametrize(
    "run_number",
    range(30),  # run the test multiple times to detect race conditions
)
def test_close_channel(run_number: int):
    pc1, pc2 = _create_peer_connections()

    pc1_dc_open_evt = threading.Event()
    pc1_dc_closed_evt = threading.Event()
    message_queue = queue.Queue[str | bytes]()

    def _on_channel(channel: DataChannel):
        def _on_open():
            channel.send("hello")
            channel.send(b"not gonna read this")

        channel.on_open(_on_open)

    def _on_message(msg: str | bytes):
        message_queue.put(msg)

    pc2.on_data_channel(_on_channel)

    pc1_dc = pc1.create_data_channel("test")
    pc1_dc.on_open(pc1_dc_open_evt.set)
    pc1_dc.on_message(_on_message)
    pc1_dc.on_closed(pc1_dc_closed_evt.set)

    pc1_dc_open_evt.wait(timeout=2)

    assert pc1_dc.is_open
    assert pc1.state == State.CONNECTED
    assert pc2.state == State.CONNECTED

    msg = message_queue.get(timeout=2)

    del msg
    pc1_dc.close()

    pc1_dc_closed_evt.wait(timeout=2)
