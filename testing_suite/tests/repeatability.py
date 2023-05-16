from dto.test_result import TestResult
from testing_suite.tests.test_base import Test
from utils.poses import POSES
from utils.robotic_arm import Arm
from utils.utils import input_getter


class RepeatabilityTest(Test):
    def __init__(self, robotic_arm: Arm, repeat_times: int):
        super().__init__(robotic_arm)
        self._repeat_times = repeat_times
        self._repeat_counter = 1

    # move to grasp the "holder"
    def pre_test(self):
        self._is_finished = False
        self._arm.move_cartesian(*POSES.ABOVE_PAYLOAD_TCP_POSE_1, add_to_history=True)
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1)

    # lift gripper up
    def perform_test(self):
        if self._repeat_counter == 1:
            print(f"Please place {self._object.name} in the marked spot and press ENTER.")
            _ = input()
        self._arm.move_cartesian(*POSES.get_engagement_pose(self._gripper, self._object, 1))
        self._gripper.close()
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1)
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_2)
        # self.continue_test_step()
        self._arm.move_cartesian(*POSES.get_engagement_pose(self._gripper, self._object, 2))
        self._gripper.open()
        # self.continue_test_step()
        self._gripper.close()
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_2)
        self._arm.move_cartesian(*POSES.LOWER_PAYLOAD_TCP_POSE_1)
        # self.continue_test_step()
        self._arm.move_cartesian(*POSES.get_engagement_pose(self._gripper, self._object, 1))
        self._gripper.open()

    # todo: maybe add some automatical offset checker
    def post_test(self):
        # print("Was test successfull? y/n")
        # letter = input_getter(["y", "n"], str)
        success = True
        self.test_result.runs_data.append(
            {
                "object": self._object.name,
                "success": success,
                "try": self._repeat_counter
            }
        )
        if self._repeat_counter == self._repeat_times or not success:
            self._is_finished = True
        else:
            self._repeat_counter += 1

    # reset to initial position
    def finish_testing(self, last_gripper: bool) -> TestResult:
        if last_gripper:
            self._arm.back_to_comfortable_pose()
        self._repeat_counter = 1
        return self.test_result
    
    def continue_test_step(self):
        print("Press ENTER to continue test")
        _ = input()
