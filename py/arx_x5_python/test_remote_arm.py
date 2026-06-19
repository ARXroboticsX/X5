import time

from bimanual import SingleArm

# 1 3
# 2 4

def main():
    # 2 master arms (type=1, x5_master.urdf) on can2/can4
    master_left_config = {"can_port": "can2", "type": 2}
    master_right_config = {"can_port": "can4", "type": 2}

    # 2 slave arms (type=0, x5.urdf) on can1/can3
    # 0>2023  2>2025
    slave_left_config = {"can_port": "can1", "type": 2}
    slave_right_config = {"can_port": "can3", "type": 2}

    master_left = SingleArm(master_left_config)
    master_right = SingleArm(master_right_config)
    slave_left = SingleArm(slave_left_config)
    slave_right = SingleArm(slave_right_config)

    master_left.gravity_compensation()
    master_right.gravity_compensation()

    dt = 0.05  # 50ms

    try:
        while True:
            # Read master joint positions
            left_pos = master_left.get_joint_positions()
            right_pos = master_right.get_joint_positions()

            # Send to slaves
            slave_left.set_joint_positions(left_pos)
            slave_left.set_gripper_pos(left_pos[6])
            slave_right.set_joint_positions(right_pos)
            slave_right.set_gripper_pos(right_pos[6])

            time.sleep(dt)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        master_left.go_home()
        master_right.go_home()
        slave_left.go_home()
        slave_right.go_home()


if __name__ == "__main__":
    main()
