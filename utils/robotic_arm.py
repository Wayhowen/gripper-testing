import time

from urx import Robot


# TODO: check how to use it
class Arm:
    def __init__(self, payload_weight):
        self.robot = Robot("192.168.0.100")
        self.robot.set_tcp((0, 0, 0.1, 0, 0, 0))
        self.robot.set_payload(payload_weight)
        time.sleep(0.2)  # leave some time to robot to process the setup commands

    def update_weight(self, new_weight: float):
        self.robot.set_payload(new_weight)
        time.sleep(0.2)
