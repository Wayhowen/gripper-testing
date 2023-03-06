import traceback

from grippers.three_finger_gripper import ThreeFingerGripper
from testing_suite.tests.payload import PayloadTest
from testing_suite.tests.repeatability import RepeatabilityTest
from testing_suite.tests.tilt import TiltTest
from utils.csv_writer import CSVWriter
from utils.objects import OBJECTS
from utils.poses import POSES
from utils.robotic_arm import Arm


class TestingSuite:
    def __init__(self, initial_pose="comfy"):
        self._robotic_arm = Arm(0, speed=0.5, acceleration=0.1, initial_pose=initial_pose)
        self._test_setups = [
            #(
            #    PayloadTest(self._robotic_arm, initial_payload_weight=120.0),
            #    [OBJECTS.GLASS_BALL]
            #),
            (
                RepeatabilityTest(self._robotic_arm, 5),
                [OBJECTS.GLASS_BALL]
            ),
            #   (
            #     TiltTest(self._robotic_arm),
            #     [OBJECTS.GLASS_BALL]
            #   )
        ]

        # TODO: update gripper weight
        self._grippers = [
            ThreeFingerGripper(0.12, 0, 0, 0.150, bluetooth_connected=True),
        ]

        self._csv_writer = CSVWriter()

    def run_tests(self):
        test_result = []
        try:
            for gripper in self._grippers:
                for test, objects in self._test_setups:
                    for obj in objects:
                        test.set_gripper(gripper)
                        test.set_object(obj)

                        print(f"Pre-testing of {test.name}")
                        test.pre_test()
                        test_iteration = 1
                        while not test.is_finished:
                            print(f"Testing run {test_iteration}")
                            test.perform_test()
                            print(f"Running post test scripts")
                            test.post_test()
                            test_iteration += 1
                        print(f"Testing of {test.name} finished")
                        test_result.append(test.finish_testing(last_gripper=obj == objects[-1]))
                    self._csv_writer.save_test_results(test_result)
                    test_result = []
        except Exception as e:
            traceback.print_exc()
            self._csv_writer.save_test_results(test_result)
        finally:
            self._robotic_arm.stop(home=True)

    def set_gripper_change_pose(self):
        try:
            self._robotic_arm.move(*POSES.GRIPPER_CHANGE_POSE, add_to_history=True)
            print("press enter to finish")
            _ = input()
            self._robotic_arm.stop()
        finally:
            self._robotic_arm.stop(home=True)
