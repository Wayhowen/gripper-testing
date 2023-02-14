from testing_suite.tests.test_base import Test
from utils.robotic_arm import Arm

ABOVE_PAYLOAD_TCP_POSE = [-0.6, -0.109, 0.35, 2.22, 2.22, 0]
ENGAGEMENT_TCP_POSE = [-0.6, -0.109, 0.03, 2.22, 2.22, 0]
# comments from their code - # pi/2, -1.7947, 1.2356, pi -1.033, -pi/2 which is -1.5710, 0.0051
COMFORTABLE_POSE = [0, -1.9049, 1.9520, -1.6088, -3.14/2, 0]


class PayloadTest(Test):
    def __init__(self, robotic_arm: Arm):
        super().__init__(robotic_arm)

    # move to grasp the "holder"
    def pre_test(self):
        print("pre test")
        self._arm.move(*COMFORTABLE_POSE, add_to_history=True)
        self._arm.move_cartesian(*ABOVE_PAYLOAD_TCP_POSE, add_to_history=True)
        self._arm.move_cartesian(*ENGAGEMENT_TCP_POSE, add_to_history=True)

    # lift holder up
    def perform_test(self):
        self._arm.move_cartesian(*ABOVE_PAYLOAD_TCP_POSE)
        self._arm.move_cartesian(*ENGAGEMENT_TCP_POSE)

    # place holder down on the ground and wait for input telling whether to continue or not
    def post_test(self):
        self._is_finished = True

    # reset to initial position
    def finish_testing(self):
        self._arm.home()
