from abc import abstractmethod


class Gripper:
    # TODO: possibly change those values to the ones we will use in actual testing
    def __init__(self, height, width, length, gripper_weight: float):
        self.height = height
        self.width = width
        self.length = length

        self._gripper_state = None

    @property
    def gripper_open(self):
        return self._gripper_state == "open"

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def open(self):
        raise NotImplementedError
