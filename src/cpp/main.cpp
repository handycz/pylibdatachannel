#include "pybind11/pybind11.h"
#include "pybind11/stl.h"
#include "pybind11/functional.h"
#include "rtc/rtc.hpp"
#include "rtc/common.hpp"

namespace py = pybind11;

const std::string moduleName = "_pylibdatachannel";

/*
* Pybind11 module definition
*/
PYBIND11_MODULE(_pylibdatachannel, m) {
  /*
   * PeerConnectionInterface Enums
   */
	py::enum_<rtc::PeerConnection::SignalingState>(m, "SignalingState")
		.value("STABLE", rtc::PeerConnection::SignalingState::Stable)
		.value("HAVELOCALOFFER", rtc::PeerConnection::SignalingState::HaveLocalOffer)
		.value("HAVELOCALPRANSWER", rtc::PeerConnection::SignalingState::HaveLocalPranswer)
		.value("HAVEREMOTEOFFER", rtc::PeerConnection::SignalingState::HaveRemoteOffer)
		.value("HAVEREMOTEPRANSWER", rtc::PeerConnection::SignalingState::HaveRemotePranswer);

	py::enum_<rtc::PeerConnection::GatheringState>(m, "GatheringState")
		.value("NEW", rtc::PeerConnection::GatheringState::New)
		.value("GATHERING", rtc::PeerConnection::GatheringState::InProgress)
		.value("COMPLETE", rtc::PeerConnection::GatheringState::Complete);

	py::enum_<rtc::PeerConnection::State>(m, "State")
		.value("NEW", rtc::PeerConnection::State::New)
		.value("CONNECTING", rtc::PeerConnection::State::Connecting)
		.value("CONNECTED", rtc::PeerConnection::State::Connected)
		.value("DISCONNECTED", rtc::PeerConnection::State::Disconnected)
		.value("FAILED", rtc::PeerConnection::State::Failed)
		.value("CLOSED", rtc::PeerConnection::State::Closed);

	py::enum_<rtc::PeerConnection::IceState>(m, "IceState")
		.value("NEW", rtc::PeerConnection::IceState::New)
		.value("CHECKING", rtc::PeerConnection::IceState::Checking)
		.value("CONNECTED", rtc::PeerConnection::IceState::Connected)
		.value("COMPLETED", rtc::PeerConnection::IceState::Completed)
		.value("FAILED", rtc::PeerConnection::IceState::Failed)
		.value("DISCONNECTED", rtc::PeerConnection::IceState::Disconnected)
		.value("CLOSED", rtc::PeerConnection::IceState::Closed);

	py::enum_<rtc::Description::Type>(m, "DescriptionType")
		.value("UNSPEC", rtc::Description::Type::Unspec)
		.value("OFFER", rtc::Description::Type::Offer)
		.value("ANSWER", rtc::Description::Type::Answer)
		.value("PRANSWER", rtc::Description::Type::Pranswer)
		.value("ROLLBACK", rtc::Description::Type::Rollback)
		.def_static("from_string", &rtc::Description::stringToType);

	py::enum_<rtc::IceServer::RelayType>(m, "IceServerRelayType")
		.value("TURN_UDP", rtc::IceServer::RelayType::TurnUdp)
		.value("TURN_TCP", rtc::IceServer::RelayType::TurnTcp)
		.value("TURN_TLS", rtc::IceServer::RelayType::TurnTls);

	py::enum_<rtc::IceServer::Type>(m, "IceServerType")
		.value("STUN", rtc::IceServer::Type::Stun)
		.value("TURN", rtc::IceServer::Type::Turn);

 /*
  * IceServer
  */
	py::class_<rtc::IceServer>(m, "IceServer")
	 // turn constructor
	 .def(py::init([](std::string hostname, int port, std::string username, std::string password, rtc::IceServer::RelayType relay_type) {
	  	 return rtc::IceServer(hostname, port, username, password, relay_type);
	 }), py::return_value_policy::move, py::arg("hostname"), py::arg("port"), py::arg("username"), py::arg("password"), py::arg("relay_type"))
	 // stun constructor
	 .def(py::init([](std::string hostname, int port) {
			 return rtc::IceServer(hostname, port);
	 }), py::return_value_policy::move, py::arg("hostname"), py::arg("port"))
	 .def("__repr__", [](const rtc::IceServer &a) {
		 return "<" + moduleName + ".IceServer url='" + a.hostname + "' username='" + a.username + "' password='" + a.password + "'>";
	 })
	 .def_readonly("hostname", &rtc::IceServer::hostname)
	 .def_readonly("port", &rtc::IceServer::port)
	 .def_readonly("username", &rtc::IceServer::username)
	 .def_readonly("password", &rtc::IceServer::password)
	 .def_readonly("relay_type", &rtc::IceServer::relayType)
	 .def_readonly("type", &rtc::IceServer::type);

  /*
   * RTCConfiguration
   */
  py::class_<rtc::Configuration>(m, "Configuration")
    .def(py::init([](std::vector<rtc::IceServer> ice_servers) {
      return rtc::Configuration{.iceServers = ice_servers};
    }), py::return_value_policy::move, py::arg("ice_servers"))
    .def_readonly("ice_servers", &rtc::Configuration::iceServers);

 /*
  * Candidate
  */
  py::class_<rtc::Candidate>(m, "Candidate")
    .def(py::init([](std::string &candidate, std::string mid) {
      return rtc::Candidate(candidate, mid);
    }), py::return_value_policy::move, py::arg("candidate"), py::arg("mid"))
    .def_property_readonly("candidate", [](const rtc::Candidate &self) {
      return std::string(self);
    }, py::return_value_policy::move)
    .def_property_readonly("mid", [](const rtc::Candidate &self) {
      return self.mid();
    }, py::return_value_policy::move)
    .def("__str__", [](const rtc::Candidate &self) {
			return std::string(self);
		});

 /*
  * SessionDescriptionInterface
  */
	py::class_<rtc::Description>(m, "Description")
		.def(py::init([](std::string sdp, rtc::Description::Type type) {
			return rtc::Description(sdp, type);
		}), py::return_value_policy::move, py::arg("sdp"), py::arg("type"))
		.def_property_readonly("type", [](const rtc::Description &self) {
			return self.type();
		}, py::return_value_policy::move)
		.def_property_readonly("description", [](const rtc::Description &self) {
			return std::string(self);
		}, py::return_value_policy::move)
		.def("__str__", [](const rtc::Description &self) {
			return std::string(self);
		});

 /*
  * DataChannel
	*/
	py::class_<rtc::DataChannel, std::shared_ptr<rtc::DataChannel>>(m, "DataChannel")
		.def_property_readonly("label", &rtc::DataChannel::label)
		.def_property_readonly("is_open", [](const rtc::DataChannel &self) {
			return self.isOpen();
		})
		.def("on_open", &rtc::DataChannel::onOpen, py::arg("callback"), py::keep_alive<1, 2>())
		.def("on_closed", &rtc::DataChannel::onClosed, py::arg("callback"), py::keep_alive<1, 2>())
		.def("on_error", &rtc::DataChannel::onError, py::arg("callback"), py::keep_alive<1, 2>())
		.def("on_message", [](rtc::DataChannel &self, std::function<void(std::variant<std::string, std::vector<uint8_t>> data)> callback) {
			self.onMessage(
				[callback](rtc::binary data) {
					std::vector<uint8_t> bytes;
					bytes.reserve(data.size());
					for (std::byte b : data) {
						bytes.push_back(static_cast<uint8_t>(b));
					}

					callback(
						std::variant<std::string, std::vector<uint8_t>>(bytes)
					);
				},
				[callback](std::string data) {
					callback(
						std::variant<std::string, std::vector<uint8_t>>(data)
					);
				}
			);
	}, py::arg("callback"),
	"Register callback evoked when a message is received. The callback is provided with either `str` or a list of integers representing `bytes`."
	)
	.def("send", [](rtc::DataChannel &self, std::variant<py::str, py::bytes> data) {
		if (std::holds_alternative<py::bytes>(data)) {
			std::string pyBytes = std::get<py::bytes>(data);
			std::vector<std::byte> bytes;
			for (char b : pyBytes) {
				bytes.push_back(static_cast<std::byte>(b));
			}
			self.send(bytes);
		}
		else {
			py::str pyStr = std::get<py::str>(data);
			std::string str = std::string(pyStr);
			self.send(str);
		}
	}, py::arg("data"),
	"Send a message to the remote peer. The message can be either a `str` or `bytes`."
	)
	.def("reset_callbacks", &rtc::DataChannel::resetCallbacks)
	.def("close", &rtc::DataChannel::close);

 /*
  * PeerConnectionInterface
  */
	py::class_<rtc::PeerConnection, std::shared_ptr<rtc::PeerConnection>>(m, "PeerConnection")
	 .def(py::init([](const std::optional<rtc::Configuration> configuration) {
			return std::make_shared<rtc::PeerConnection>(
				configuration.value()
			);
	 }), py::arg("configuration"))
	 .def(py::init([]() {
				return std::make_shared<rtc::PeerConnection>();
	 }))
	 .def("set_local_description", [](rtc::PeerConnection &self, rtc::Description::Type type) {
		 self.setLocalDescription(type);
	 }, py::arg("type"))
	 .def("set_remote_description", [](rtc::PeerConnection& self, rtc::Description &description) {
		 self.setRemoteDescription(description);
	 }, py::arg("description"))
	 .def("add_remote_candidate", [](rtc::PeerConnection &self, rtc::Candidate &candidate) {
		 self.addRemoteCandidate(candidate);
	 }, py::arg("candidate"))
	 .def("create_data_channel", [](rtc::PeerConnection &self, std::string &label) {
		 return self.createDataChannel(label);
	 }, py::arg("label"), py::keep_alive<1, 0>())
	 .def("on_data_channel", &rtc::PeerConnection::onDataChannel, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_local_description", &rtc::PeerConnection::onLocalDescription, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_local_candidate", &rtc::PeerConnection::onLocalCandidate, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_state_change", &rtc::PeerConnection::onStateChange, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_ice_state_change", &rtc::PeerConnection::onIceStateChange, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_gathering_state_change", &rtc::PeerConnection::onGatheringStateChange, py::arg("callback"), py::keep_alive<1, 2>())
	 .def("on_signaling_state_change", &rtc::PeerConnection::onSignalingStateChange, py::arg("callback"), py::keep_alive<1, 2>())
   .def("reset_callbacks", &rtc::PeerConnection::resetCallbacks)
	 .def("close", &rtc::PeerConnection::close)
	 .def_property_readonly("signaling_state", [](const rtc::PeerConnection &self) {
			return self.signalingState();
		})
	 .def_property_readonly("ice_state", [](const rtc::PeerConnection &self) {
			return self.iceState();
		})
	 .def_property_readonly("state", [](const rtc::PeerConnection &self) {
			return self.state();
		})
	 .def_property_readonly("ice_connection_state", [](const rtc::PeerConnection &self) {
			return self.iceState();
		})
	 .def_property_readonly("local_description", [](const rtc::PeerConnection &self) {
			return self.localDescription().value();
		})
	 .def_property_readonly("remote_description", [](const rtc::PeerConnection &self) {
			return self.remoteDescription().value();
		});
}
