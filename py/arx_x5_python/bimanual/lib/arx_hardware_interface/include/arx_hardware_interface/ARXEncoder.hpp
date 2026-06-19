//
// Created by yezi on 2025/9/27.
//

#pragma once

#include "arx_hardware_interface/canbase/CanBaseDef.hpp"

namespace arx {
namespace hw_interface {
class ARXEncoder {
 public:
  void read(CanFrame *frame);
  void getValue(double *joint);
  void update();

 private:
  double joint_[8]{0, 0, 0, 0, 0, 0, 0, 0};
  double joint_buffer_[8]{0, 0, 0, 0, 0, 0, 0, 0};
};
} // namespace hw_interface
} // namespace arx