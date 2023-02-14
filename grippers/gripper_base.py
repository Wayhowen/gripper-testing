from abc import abstractmethod

from utils.robotic_arm import Arm


class Gripper:
    # TODO: possibly change those values to the ones we will use in actual testing
    def __init__(self, height, width, length, gripper_weight: float, arm_connected: bool):
        self.height = height
        self.width = width
        self.length = length

        self._gripper_state = None

        self.arm = Arm(gripper_weight) if arm_connected else None

    @property
    def gripper_open(self):
        return self._gripper_state == "open"

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def open(self):
        raise NotImplementedError
