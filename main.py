from testing_suite.testing_suite import TestingSuite


class Main:
    def __init__(self):
        self._testing_suite = TestingSuite()

    def run(self):
        self._testing_suite.run_tests()


if __name__ == '__main__':
    main = Main()
    main.run()
