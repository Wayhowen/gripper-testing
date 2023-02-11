from grippers.gripper_base import Gripper


class ThreeFingerGripper(Gripper):
    def __init__(self, height, width, length):
        super().__init__(height, width, length)

    def open(self):
        pass

    def close(self):
        pass
