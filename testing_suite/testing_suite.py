import traceback

from grippers.three_finger_gripper import ThreeFingerGripper
from testing_suite.tests.payload import PayloadTest
from utils.csv_writer import CSVWriter
from utils.robotic_arm import Arm


class TestingSuite:
    def __init__(self):
        self._robotic_arm = Arm(0)
        self._tests_list = [
            PayloadTest(self._robotic_arm, initial_payload_weight=0.0)
        ]

        # TODO: update gripper weight
        self._grippers = [
            ThreeFingerGripper(0, 0, 0, 0.150)
        ]
        self._csv_writer = CSVWriter()

    def run_tests(self):
        try:
            for gripper in self._grippers:
                for test in self._tests_list:
                    test.set_gripper(gripper)

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
                    result = test.finish_testing()
                    self._csv_writer.save_test_results([result])
        except Exception as e:
            traceback.print_exc()
        finally:
            self._robotic_arm.stop(home=True)
