import time
import traceback

from urx import Robot

BASE = 0
SHOULDER = -1.57
ELBOW = 0
WRIST_1 = -1.57
WRIST_2 = 0
WRIST_3 = 0

# POSES IN LINEAR SPACE
HOME = [BASE, SHOULDER, ELBOW, WRIST_1, WRIST_2, WRIST_3]
PICKUP_POSE = [0, -1.57, 1.57, -1.57, -1.57, 0]

# POSES IN TCP SPACE
# Z in this positions is fucked up
COMFORTABLE_TCP_POSE = [-0.347, -0.109, 0.35, 2.22, 2.22, 0]
ABOVE_PAYLOAD_TCP_POSE = [-0.6, -0.109, 0.35, 2.22, 2.22, 0]
ENGAGEMENT_TCP_POSE = [-0.6, -0.109, 0.03, 2.22, 2.22, 0]


class Arm:
    def __init__(self, payload_weight, speed=1.5, acceleration=0.3):
        self.robot = Robot("192.168.56.10")
        self._speed = speed
        self._acceleration = acceleration
        #self.robot.set_tcp((0, 0, 0.1, 0, 0, 0))
        # self.robot.set_payload(payload_weight)
        time.sleep(0.5)  # leave some time to robot to process the setup commands
        # self.move(BASE, SHOULDER, ELBOW, WRIST_1, WRIST_2, WRIST_3)
        self._command_memory = []

    def update_weight(self, new_weight: float):
        self.robot.set_payload(new_weight)
        time.sleep(0.2)

    def home(self):
        for command in self._command_memory[::-1]:
            if command[0] == "j":
                self.move(*command[1])
            elif command[0] == "l":
                self.move_cartesian(*command[1])
        self._command_memory = []

    def move(self, base, shoulder, elbow, wrist_1, wrist_2, wrist_3, add_to_history=False):
        if add_to_history:
            self._command_memory.append(("j", self.robot.getj()))
        self.robot.movej([base, shoulder, elbow, wrist_1, wrist_2, wrist_3], vel=self._speed, acc=self._acceleration)

    def move_cartesian(self, x, y, z, rx, ry, rz, add_to_history=False):
        if add_to_history:
            self._command_memory.append(("l", self.robot.getl()))
        self.robot.movel([x, y, z, rx, ry, rz], vel=self._speed, acc=self._acceleration)

    def stop(self):
        self.robot.close()


if __name__ == '__main__':
    # try:
    a = Arm(0)
    try:
        # a.move(*COMFORTABLE_POSE)
        # a.robot.stopj()
        # print(*TEST_TCP_POSE)
        a.move_cartesian(*ENGAGEMENT_TCP_POSE)
        print(a.robot.getl())
        # a.robot.stopl()
    except Exception as e:
        traceback.print_exc()
    finally:
        a.robot.close()
    # except Exception as e:
    #     print(traceback.print_exc())
    # finally:
    # a.robot.stopj()