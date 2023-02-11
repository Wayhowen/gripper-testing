from abc import abstractmethod


class Gripper:
    # TODO: possibly change those values to the ones we will use in actual testing
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def open(self):
        raise NotImplementedError
