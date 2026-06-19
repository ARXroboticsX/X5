import time
import sys
import os

from bimanual import SingleArm
import encoder_interface

# 1 3
# 2 4

def main():
    # 2 encoder instances on can2/can4 (master side)
    encoder_left = encoder_interface.EncoderInterface("can2")
    encoder_right = encoder_interface.EncoderInterface("can4")

    # 2 slave arms (type=0, x5.urdf) on can1/can3
    # 0>2023  2>2025
    slave_left_config = {"can_port": "can1", "type": 2}
    slave_right_config = {"can_port": "can3", "type": 2}

    slave_left = SingleArm(slave_left_config)
    slave_right = SingleArm(slave_right_config)

    dt = 0.05  # 50ms

    try:
        while True:
            # Read encoder positions
            left_pos = encoder_left.get_joint_positions()
            right_pos = encoder_right.get_joint_positions()
            left_pos[3] *= -1
            left_pos[6] *= 2.78
            left_pos[6] = -abs(left_pos[6])
            right_pos[3] *= -1
            right_pos[6] *= 2.78
            right_pos[6] = -abs(right_pos[6])

            # Send to slave arms
            slave_left.set_joint_positions(left_pos)
            slave_left.set_gripper_pos(left_pos[6])
            slave_right.set_joint_positions(right_pos)
            slave_right.set_gripper_pos(right_pos[6])

            time.sleep(dt)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        slave_left.go_home()
        slave_right.go_home()


if __name__ == "__main__":
    main()
