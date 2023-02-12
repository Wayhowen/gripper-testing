from grippers.three_finger_gripper import ThreeFingerGripper
from testing_suite.tests.payload import PayloadTest


class TestingSuite:
    def __init__(self):
        self._tests_list = [
            PayloadTest()
        ]

        # TODO: update gripper weight
        self._grippers = [
            ThreeFingerGripper(0, 0, 0, 0.150)
        ]

    def run_tests(self):
        for gripper in self._grippers:
            for test in self._tests_list:
                test.set_gripper(gripper)

                while not test.is_finished:
                    test.pre_test()
                    test.perform_test()
                    test.post_test()


