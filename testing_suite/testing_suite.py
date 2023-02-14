import traceback

from grippers.three_finger_gripper import ThreeFingerGripper
from testing_suite.tests.payload import PayloadTest
from utils.robotic_arm import Arm


class TestingSuite:
    def __init__(self):
        self._robotic_arm = Arm(0)
        self._tests_list = [
            PayloadTest(self._robotic_arm)
        ]

        # TODO: update gripper weight
        self._grippers = [
            ThreeFingerGripper(0, 0, 0, 0.150)
        ]

    def run_tests(self):
        try:
            for gripper in self._grippers:
                for test in self._tests_list:
                    test.set_gripper(gripper)

                    test.pre_test()
                    while not test.is_finished:
                        test.perform_test()
                        test.post_test()
                    test.finish_testing()
        except Exception as e:
            traceback.print_exc()
        finally:
            self._robotic_arm.stop()
