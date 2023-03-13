import math

from dto.test_result import TestResult
from testing_suite.tests.test_base import Test
from utils.poses import POSES
from utils.robotic_arm import Arm
from utils.utils import input_getter


class TiltTest(Test):
    def __init__(self, robotic_arm: Arm):
        super().__init__(robotic_arm)
        self.angle = 0
        self.amount_to_lower = 0

    # move to grasp the "holder"
    def pre_test(self):
        self._is_finished = False
        self._arm.move_cartesian(*POSES.ABOVE_PAYLOAD_TCP_POSE_1, add_to_history=True)
        # self._arm.tilt_wrist(90)
        # self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1, add_to_history=True)

    # TODO: work with movep
    # TODO: do we want leaving object on the ground also?
    def perform_test(self):
        print("Please provide the angle to test with as int:")
        self.angle = input_getter(None, int)
        prev_pose = self._arm.robot.getl()

        self._arm.tilt(self.angle)
        current_tcp_pose = self._arm.robot.getl()
        engagement_pose = POSES.get_engagement_pose_at_current_angle(
            prev_pose,
            current_tcp_pose,
            self._gripper,
            self._object
        )

        self._arm.move_cartesian(*engagement_pose)

        while True:
            print("Is arm low enough ? y/n")
            letter = input_getter(["y", "n"], str)
            if letter == "y":
                break
            print("Please provide float to say how much more to lower the arm")
            lower_by = input_getter(None, float)
            print(self.angle)
            base = lower_by*math.sin(math.radians(self.angle))
            print(base)
            height = math.sqrt(lower_by**2-base**2)
            print(height)

            self._arm.lower_arm(-height, -base)
            self.amount_to_lower += lower_by
        self._gripper.close()
        self._arm.move_cartesian(*current_tcp_pose)
        print("Press ENTER to release object")
        _ = input()
        self._gripper.open()
        self._arm.tilt(-self.angle)

    # place holder down on the ground and wait for input telling whether to continue or not
    def post_test(self):
        print("Was test successfull? y/n")
        letter = input_getter(["y", "n"], str)
        success = True if letter == "y" else False
        self.test_result.runs_data.append(
            {
                "tilt": self.angle,
                "success": success,
                "lowered_by": self.amount_to_lower
            }
        )
        self.amount_to_lower = 0
        self._is_finished = not success

    # reset to initial position
    def finish_testing(self, *args, **kwargs) -> TestResult:
        self._arm.back_to_comfortable_pose()
        return self.test_result
