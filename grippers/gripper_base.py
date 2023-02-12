from abc import abstractmethod

from utils.robotic_arm import Arm


class Gripper:
    # TODO: possibly change those values to the ones we will use in actual testing
    def __init__(self, height, width, length, gripper_weight: float):
        self.height = height
        self.width = width
        self.length = length

        self.arm = Arm(gripper_weight)

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def open(self):
        raise NotImplementedError
