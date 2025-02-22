from mobilegello.gello_controller import GELLOcontroller
import time


# make_hdf5("lift_data")

mygello = GELLOcontroller("doodle", torque_start=True)
mygello.goto_home()

# mygello.set_goal_joint_angles([3.14, -1.57, -1.57, 0, 0, 3.14], radians=True)

# print(mygello.read_ee_position())
# print(mygello.read_joint_position(degrees=True))
# print(mygello.read_joint_position)
print(mygello.read_encoder_values())


# mygello.teleop()