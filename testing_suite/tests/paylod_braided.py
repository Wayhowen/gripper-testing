from dto.test_result import TestResult
from testing_suite.tests.test_base import Test
from utils.poses import POSES
from utils.robotic_arm import Arm
from utils.utils import input_getter


class PayloadBraidedTest(Test):
    def __init__(self, robotic_arm: Arm, initial_payload_weight):
        super().__init__(robotic_arm)
        self.payload_weight = initial_payload_weight

    # move to grasp the "holder"
    def pre_test(self):
        self._is_finished = False
        self._arm.move_cartesian(*POSES.ABOVE_PAYLOAD_TCP_POSE_1, add_to_history=True)
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1, add_to_history=True)

    # lift gripper up
    def perform_test(self):
        print("Please provide weight added in grams as float:")
        self.payload_weight += input_getter(None, float)
        self._arm.move_cartesian(*POSES.get_engagement_pose(self._gripper, self._object, 1))

        self._gripper.close()

        self._arm.move_cartesian(*POSES.ABOVE_PAYLOAD_HIGHER_TCP_POSE_1)
        self._gripper.open()
        while True:
            print("Is arm opened correctly ? y/n")
            letter = input_getter(["y", "n"], str)
            if letter == "y":
                break
            self._gripper.close()
            self._gripper.open()
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1)

    # place holder down on the ground and wait for input telling whether to continue or not
    def post_test(self):
        print("Was test successfull? y/n")
        letter = input_getter(["y", "n"], str)
        success = True if letter == "y" else False
        self.test_result.runs_data.append(
            {
                "weight": self.payload_weight,
                "success": success
            }
        )
        self._is_finished = not success

    # reset to initial position
    def finish_testing(self, *args, **kwargs) -> TestResult:
        self._arm.back_to_comfortable_pose()
        return self.test_result
