from abc import abstractmethod

from grippers.gripper_base import Gripper


class Test:
    def __init__(self):
        self._gripper = None
        self._is_finished = False

    def set_gripper(self, gripper: Gripper):
        self._gripper = gripper

    @property
    def is_finished(self):
        return self._is_finished

    @abstractmethod
    def pre_test(self):
        raise NotImplementedError

    @abstractmethod
    def perform_test(self):
        raise NotImplementedError

    @abstractmethod
    def post_test(self):
        raise NotImplementedError

    @abstractmethod
    def finish_testing(self):
        raise NotImplementedError
