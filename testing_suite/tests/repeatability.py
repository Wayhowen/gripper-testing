from dto.test_result import TestResult
from testing_suite.tests.test_base import Test
from utils.poses import POSES
from utils.robotic_arm import Arm
from utils.utils import input_getter


class RepeatabilityTest(Test):
    def __init__(self, robotic_arm: Arm):
        super().__init__(robotic_arm)

    # move to grasp the "holder"
    def pre_test(self):
        pass

    # lift gripper up
    def perform_test(self):
        pass

    # place holder down on the ground and wait for input telling whether to continue or not
    def post_test(self):
        pass

    # reset to initial position
    def finish_testing(self) -> TestResult:
        self._arm.back_to_comfortable_pose()
        return self.test_result
