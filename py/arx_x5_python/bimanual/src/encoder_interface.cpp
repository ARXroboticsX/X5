#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "arx_hardware_interface/canbase/SocketCan.hpp"
#include "arx_hardware_interface/ARXEncoder.hpp"

namespace py = pybind11;
using namespace arx::hw_interface;

class EncoderInterface {
public:
    EncoderInterface(const std::string& can_name) {
        can_.setCallBackFunction([&](CanFrame *frame) {
            encoder_.read(frame);
        });
        can_.setGetMsgContentFunction([&]() {
            encoder_.update();
        });
        can_.Init(can_name.c_str());
    }

    ~EncoderInterface() {
        can_.Close();
    }

    std::vector<double> get_joint_positions() {
        can_.LoadMutexMsg();
        double joint_pos[8];
        encoder_.getValue(joint_pos);
        return std::vector<double>(joint_pos, joint_pos + 7);
    }

private:
    SocketCan can_;
    ARXEncoder encoder_;
};

PYBIND11_MODULE(encoder_interface, m) {
    py::class_<EncoderInterface>(m, "EncoderInterface")
        .def(py::init<const std::string&>())
        .def("get_joint_positions", &EncoderInterface::get_joint_positions);
}
