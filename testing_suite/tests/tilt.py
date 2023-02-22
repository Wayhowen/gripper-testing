from dto.test_result import TestResult
from testing_suite.tests.test_base import Test
from utils.poses import POSES
from utils.robotic_arm import Arm
from utils.utils import input_getter


class TiltTest(Test):
    def __init__(self, robotic_arm: Arm):
        super().__init__(robotic_arm)
        self.angle = 0

    # move to grasp the "holder"
    def pre_test(self):
        self._is_finished = False
        self._arm.move_cartesian(*POSES.ABOVE_PAYLOAD_TCP_POSE_1, add_to_history=True)

    # lift gripper up
    # TODO: work with movep
    def perform_test(self):
        print("Please provide the angle to test with as int:")
        self.angle += input_getter(None, int)

        lower_pose, engagement_pose = POSES.get_poses_for_angle(self._gripper, self._object, 1, self.angle)
        print(lower_pose, engagement_pose)
        self._arm.move_cartesian(*lower_pose)
        self._arm.move_cartesian(*engagement_pose)
        self._gripper.close()
        self._arm.move_cartesian(*lower_pose)
        self._arm.move_cartesian(*engagement_pose)
        self._gripper.open()
        self._arm.move_cartesian(*lower_pose)

    # place holder down on the ground and wait for input telling whether to continue or not
    def post_test(self):
        print("Was test successfull? y/n")
        letter = input_getter(["y", "n"], str)
        success = True if letter == "y" else False
        self.test_result.runs_data.append(
            {
                "tilt": self.angle,
                "success": success
            }
        )
        self._is_finished = not success

    # reset to initial position
    def finish_testing(self, *args, **kwargs) -> TestResult:
        self._arm.back_to_comfortable_pose()
        return self.test_result
