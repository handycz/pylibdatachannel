from __future__ import annotations
import typing
__all__ = ['Candidate', 'Configuration', 'DataChannel', 'Description', 'DescriptionType', 'GatheringState', 'IceServer', 'IceServerRelayType', 'IceServerType', 'IceState', 'PeerConnection', 'SignalingState', 'State']
class Candidate:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, candidate: str, mid: str) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def candidate(self) -> str:
        ...
    @property
    def mid(self) -> str:
        ...
class Configuration:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, ice_servers: list[IceServer]) -> None:
        ...
    @property
    def ice_servers(self) -> list[IceServer]:
        ...
class DataChannel:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def close(self) -> None:
        ...
    def on_closed(self, callback: typing.Callable[[], None]) -> None:
        ...
    def on_error(self, callback: typing.Callable[[str], None]) -> None:
        ...
    def on_message(self, callback: typing.Callable[[str | list[int]], None]) -> None:
        """
        Register callback evoked when a message is received. The callback is provided with either `str` or a list of integers representing `bytes`.
        """
    def on_open(self, callback: typing.Callable[[], None]) -> None:
        ...
    def reset_callbacks(self) -> None:
        ...
    def send(self, data: str | bytes) -> None:
        """
        Send a message to the remote peer. The message can be either a `str` or `bytes`.
        """
    @property
    def is_open(self) -> bool:
        ...
    @property
    def label(self) -> str:
        ...
class Description:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, sdp: str, type: DescriptionType) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def description(self) -> str:
        ...
    @property
    def type(self) -> DescriptionType:
        ...
class DescriptionType:
    """
    Members:
    
      UNSPEC
    
      OFFER
    
      ANSWER
    
      PRANSWER
    
      ROLLBACK
    """
    ANSWER: typing.ClassVar[DescriptionType]  # value = <DescriptionType.ANSWER: 2>
    OFFER: typing.ClassVar[DescriptionType]  # value = <DescriptionType.OFFER: 1>
    PRANSWER: typing.ClassVar[DescriptionType]  # value = <DescriptionType.PRANSWER: 3>
    ROLLBACK: typing.ClassVar[DescriptionType]  # value = <DescriptionType.ROLLBACK: 4>
    UNSPEC: typing.ClassVar[DescriptionType]  # value = <DescriptionType.UNSPEC: 0>
    __members__: typing.ClassVar[dict[str, DescriptionType]]  # value = {'UNSPEC': <DescriptionType.UNSPEC: 0>, 'OFFER': <DescriptionType.OFFER: 1>, 'ANSWER': <DescriptionType.ANSWER: 2>, 'PRANSWER': <DescriptionType.PRANSWER: 3>, 'ROLLBACK': <DescriptionType.ROLLBACK: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def from_string(arg0: str) -> DescriptionType:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GatheringState:
    """
    Members:
    
      NEW
    
      GATHERING
    
      COMPLETE
    """
    COMPLETE: typing.ClassVar[GatheringState]  # value = <GatheringState.COMPLETE: 2>
    GATHERING: typing.ClassVar[GatheringState]  # value = <GatheringState.GATHERING: 1>
    NEW: typing.ClassVar[GatheringState]  # value = <GatheringState.NEW: 0>
    __members__: typing.ClassVar[dict[str, GatheringState]]  # value = {'NEW': <GatheringState.NEW: 0>, 'GATHERING': <GatheringState.GATHERING: 1>, 'COMPLETE': <GatheringState.COMPLETE: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IceServer:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, hostname: str, port: int, username: str, password: str, relay_type: IceServerRelayType) -> None:
        ...
    @typing.overload
    def __init__(self, hostname: str, port: int) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def hostname(self) -> str:
        ...
    @property
    def password(self) -> str:
        ...
    @property
    def port(self) -> int:
        ...
    @property
    def relay_type(self) -> IceServerRelayType:
        ...
    @property
    def type(self) -> IceServerType:
        ...
    @property
    def username(self) -> str:
        ...
class IceServerRelayType:
    """
    Members:
    
      TURN_UDP
    
      TURN_TCP
    
      TURN_TLS
    """
    TURN_TCP: typing.ClassVar[IceServerRelayType]  # value = <IceServerRelayType.TURN_TCP: 1>
    TURN_TLS: typing.ClassVar[IceServerRelayType]  # value = <IceServerRelayType.TURN_TLS: 2>
    TURN_UDP: typing.ClassVar[IceServerRelayType]  # value = <IceServerRelayType.TURN_UDP: 0>
    __members__: typing.ClassVar[dict[str, IceServerRelayType]]  # value = {'TURN_UDP': <IceServerRelayType.TURN_UDP: 0>, 'TURN_TCP': <IceServerRelayType.TURN_TCP: 1>, 'TURN_TLS': <IceServerRelayType.TURN_TLS: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IceServerType:
    """
    Members:
    
      STUN
    
      TURN
    """
    STUN: typing.ClassVar[IceServerType]  # value = <IceServerType.STUN: 0>
    TURN: typing.ClassVar[IceServerType]  # value = <IceServerType.TURN: 1>
    __members__: typing.ClassVar[dict[str, IceServerType]]  # value = {'STUN': <IceServerType.STUN: 0>, 'TURN': <IceServerType.TURN: 1>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IceState:
    """
    Members:
    
      NEW
    
      CHECKING
    
      CONNECTED
    
      COMPLETED
    
      FAILED
    
      DISCONNECTED
    
      CLOSED
    """
    CHECKING: typing.ClassVar[IceState]  # value = <IceState.CHECKING: 1>
    CLOSED: typing.ClassVar[IceState]  # value = <IceState.CLOSED: 6>
    COMPLETED: typing.ClassVar[IceState]  # value = <IceState.COMPLETED: 3>
    CONNECTED: typing.ClassVar[IceState]  # value = <IceState.CONNECTED: 2>
    DISCONNECTED: typing.ClassVar[IceState]  # value = <IceState.DISCONNECTED: 5>
    FAILED: typing.ClassVar[IceState]  # value = <IceState.FAILED: 4>
    NEW: typing.ClassVar[IceState]  # value = <IceState.NEW: 0>
    __members__: typing.ClassVar[dict[str, IceState]]  # value = {'NEW': <IceState.NEW: 0>, 'CHECKING': <IceState.CHECKING: 1>, 'CONNECTED': <IceState.CONNECTED: 2>, 'COMPLETED': <IceState.COMPLETED: 3>, 'FAILED': <IceState.FAILED: 4>, 'DISCONNECTED': <IceState.DISCONNECTED: 5>, 'CLOSED': <IceState.CLOSED: 6>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PeerConnection:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, configuration: Configuration | None) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    def add_remote_candidate(self, candidate: Candidate) -> None:
        ...
    def close(self) -> None:
        ...
    def create_data_channel(self, label: str) -> DataChannel:
        ...
    def on_data_channel(self, callback: typing.Callable[[DataChannel], None]) -> None:
        ...
    def on_gathering_state_change(self, callback: typing.Callable[[GatheringState], None]) -> None:
        ...
    def on_ice_state_change(self, callback: typing.Callable[[IceState], None]) -> None:
        ...
    def on_local_candidate(self, callback: typing.Callable[[Candidate], None]) -> None:
        ...
    def on_local_description(self, callback: typing.Callable[[Description], None]) -> None:
        ...
    def on_signaling_state_change(self, callback: typing.Callable[[SignalingState], None]) -> None:
        ...
    def on_state_change(self, callback: typing.Callable[[State], None]) -> None:
        ...
    def reset_callbacks(self) -> None:
        ...
    def set_local_description(self, type: DescriptionType) -> None:
        ...
    def set_remote_description(self, description: Description) -> None:
        ...
    @property
    def ice_connection_state(self) -> IceState:
        ...
    @property
    def ice_state(self) -> IceState:
        ...
    @property
    def local_description(self) -> Description:
        ...
    @property
    def remote_description(self) -> Description:
        ...
    @property
    def signaling_state(self) -> SignalingState:
        ...
    @property
    def state(self) -> State:
        ...
class SignalingState:
    """
    Members:
    
      STABLE
    
      HAVELOCALOFFER
    
      HAVELOCALPRANSWER
    
      HAVEREMOTEOFFER
    
      HAVEREMOTEPRANSWER
    """
    HAVELOCALOFFER: typing.ClassVar[SignalingState]  # value = <SignalingState.HAVELOCALOFFER: 1>
    HAVELOCALPRANSWER: typing.ClassVar[SignalingState]  # value = <SignalingState.HAVELOCALPRANSWER: 3>
    HAVEREMOTEOFFER: typing.ClassVar[SignalingState]  # value = <SignalingState.HAVEREMOTEOFFER: 2>
    HAVEREMOTEPRANSWER: typing.ClassVar[SignalingState]  # value = <SignalingState.HAVEREMOTEPRANSWER: 4>
    STABLE: typing.ClassVar[SignalingState]  # value = <SignalingState.STABLE: 0>
    __members__: typing.ClassVar[dict[str, SignalingState]]  # value = {'STABLE': <SignalingState.STABLE: 0>, 'HAVELOCALOFFER': <SignalingState.HAVELOCALOFFER: 1>, 'HAVELOCALPRANSWER': <SignalingState.HAVELOCALPRANSWER: 3>, 'HAVEREMOTEOFFER': <SignalingState.HAVEREMOTEOFFER: 2>, 'HAVEREMOTEPRANSWER': <SignalingState.HAVEREMOTEPRANSWER: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class State:
    """
    Members:
    
      NEW
    
      CONNECTING
    
      CONNECTED
    
      DISCONNECTED
    
      FAILED
    
      CLOSED
    """
    CLOSED: typing.ClassVar[State]  # value = <State.CLOSED: 5>
    CONNECTED: typing.ClassVar[State]  # value = <State.CONNECTED: 2>
    CONNECTING: typing.ClassVar[State]  # value = <State.CONNECTING: 1>
    DISCONNECTED: typing.ClassVar[State]  # value = <State.DISCONNECTED: 3>
    FAILED: typing.ClassVar[State]  # value = <State.FAILED: 4>
    NEW: typing.ClassVar[State]  # value = <State.NEW: 0>
    __members__: typing.ClassVar[dict[str, State]]  # value = {'NEW': <State.NEW: 0>, 'CONNECTING': <State.CONNECTING: 1>, 'CONNECTED': <State.CONNECTED: 2>, 'DISCONNECTED': <State.DISCONNECTED: 3>, 'FAILED': <State.FAILED: 4>, 'CLOSED': <State.CLOSED: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...