import traceback

from grippers.three_finger_gripper import ThreeFingerGripper
from testing_suite.tests.payload import PayloadTest
from testing_suite.tests.repeatability import RepeatabilityTest
from testing_suite.tests.tilt import TiltTest
from utils.csv_writer import CSVWriter
from utils.objects import OBJECTS
from utils.robotic_arm import Arm


class TestingSuite:
    def __init__(self):
        self._robotic_arm = Arm(0, speed=0.5, acceleration=0.1)
        self._test_setups = [
            # (
            #     PayloadTest(self._robotic_arm, initial_payload_weight=0.0),
            #     [OBJECTS.PAYLOAD_BOX]
            #  ),
            # (
            #     RepeatabilityTest(self._robotic_arm, 2),
            #     [OBJECTS.GLASS_BALL]
            # ),
              (
                TiltTest(self._robotic_arm),
                [OBJECTS.BALL]
              )
        ]

        # TODO: update gripper weight
        self._grippers = [
            ThreeFingerGripper(0.12, 0, 0, 0.150, bluetooth_connected=False),
        ]

        self._csv_writer = CSVWriter()

    def run_tests(self):
        try:
            test_result = []
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
        finally:
            self._robotic_arm.stop(home=True)
