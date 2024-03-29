from abc import abstractmethod

from dto.test_result import TestResult
from grippers.gripper_base import Gripper
from utils.objects import Object
from utils.robotic_arm import Arm


class Test:
    def __init__(self, robotic_arm: Arm):
        self._gripper = None
        self._object = None
        self._arm = robotic_arm
        self._is_finished = False
        self.test_result = TestResult(self.name, [])

    @property
    def name(self):
        return self.__class__.__name__

    def set_gripper(self, gripper: Gripper):
        self._gripper = gripper

    def set_object(self, obj: Object):
        self._object = obj

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
    def finish_testing(self, *args, **kwargs) -> TestResult:
        raise NotImplementedError
