from testing_suite.testing_suite import TestingSuite


class Main:
    def __init__(self, initial_pose="comfy"):
        self._testing_suite = TestingSuite(initial_pose)

    def run(self):
        self._testing_suite.run_tests()

    def set_change_pose(self):
        self._testing_suite.set_gripper_change_pose()


if __name__ == '__main__':
    main = Main()
    main.run()
    # main.set_change_pose()
