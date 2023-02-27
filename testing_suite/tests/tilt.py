import copy
import math
import time

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
        # self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1, add_to_history=True)

        self._arm.robot.movel((0, 0, 0, -0.3, 0, 0), relative=True)
        current_pos = self._arm.robot.getl()
        new_p = [*POSES.get_engagement_pose(self._gripper, self._object, 1)[:3], *current_pos[3:]]
        self._arm.move_cartesian(*new_p)
        # self._arm.robot.movel((0, 0, -0.2, 0, 0, 0), relative=True)
        # orient = self._arm.robot.get_orientation()
        # orient.rotate_z -= 0.3
        # self._arm.robot.set_orientation(orient)
        # self._arm.robot.((0, 0, -l), acc=a, vel=v)
        # t = self._arm.robot.get_pose()
        # t.orient.rotate(0.3)
        # self._arm.robot.set_pose(t)
        # self._arm.robot.movel_tool(*POSES.LOWER_PAYLOAD_TCP_POSE_1)
        # p = POSES.ABOVE_PAYLOAD_TCP_POSE_1
        # p[3] -= 1.57
        # p[4] -= 1.57
        # p[5] -= 1.57

        # self._arm.move_cartesian(*p)
        # new_p = copy.copy(p)
        # new_p[2] -= 0.02
        # self._arm.move_cartesian(*new_p)


    # lift gripper up
    # TODO: work with movep
    def perform_test(self):
        print("Please provide the angle to test with as int:")
        self.angle = input_getter(None, int)

        # self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1)
        # self._arm.interactive_test()
        # self._arm.tilt(self.angle)
        # lower_pose, engagement_pose = POSES.get_poses_for_angle(self._gripper, self._arm.robot.getl(), self._arm.robot.getj(), self._object, 1, self.angle)
        # print(lower_pose, engagement_pose)
        # self._arm.move_cartesian(*lower_pose)
        # self._arm.move_cartesian(*engagement_pose)
        # self._arm.interactive_test()
        # self._arm.move_cartesian(*engagement_pose)
        # self._gripper.close()
        # self._arm.move_cartesian(*lower_pose)
        # self._arm.move_cartesian(*engagement_pose)
        # self._gripper.open()
        # self._arm.move_cartesian(*lower_pose)

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
