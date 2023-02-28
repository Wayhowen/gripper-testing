import math
import time
import traceback

from urx import Robot

from utils.poses import POSES
from utils.utils import input_getter


class Arm:
    def __init__(self, payload_weight, speed=1.5, acceleration=0.3, initial_pose="comfy"):
        try:
            self.robot = Robot("192.168.56.10")
            self._speed = speed
            self._acceleration = acceleration
            #self.robot.set_tcp((0, 0, 0.1, 0, 0, 0))
            # self.robot.set_payload(payload_weight)
            time.sleep(1)  # leave some time to robot to process the setup commands
            # self.move(BASE, SHOULDER, ELBOW, WRIST_1, WRIST_2, WRIST_3)
            self._command_memory = []

            if initial_pose == "comfy":
                self.move(*POSES.COMFORTABLE_POSE)
                print(self.robot.getl())
            else:
                self.move(*POSES.GRIPPER_CHANGE_POSE)
        except Exception as e:
            print("Connection exception, closing")
            self.stop()

    def update_weight(self, new_weight: float):
        self.robot.set_payload(new_weight)
        time.sleep(0.2)

    def back_to_comfortable_pose(self):
        for command in self._command_memory[::-1]:
            if command[0] == "j":
                self.move(*command[1])
            elif command[0] == "l":
                self.move_cartesian(*command[1])
            elif command[0] == "p":
                self.move_p(*command[1])
        self.clear_memory()

    def clear_memory(self):
        self._command_memory = []

    def add_to_memory(self, position_type: str):
        if position_type == "j":
            self._command_memory.append(("j", self.robot.getj()))
        elif position_type == "l":
            self._command_memory.append(("l", self.robot.getl()))
        elif position_type == "p":
            # TODO: verify if its get pose
            self._command_memory.append(("p", self.robot.get_pose()))
        else:
            raise NotImplementedError

    def move(self, base, shoulder, elbow, wrist_1, wrist_2, wrist_3, add_to_history=False):
        if add_to_history:
            self.add_to_memory("j")
        self.robot.movej([base, shoulder, elbow, wrist_1, wrist_2, wrist_3], vel=self._speed, acc=self._acceleration)

    def tilt(self, tilt_angle):
        self.robot.movel(
            (0, 0, 0, -math.tan(math.radians(tilt_angle)), 0, 0),
            vel=self._speed,
            acc=self._acceleration,
            relative=True
        )

    def move_cartesian(self, x, y, z, rx, ry, rz, add_to_history=False):
        if add_to_history:
            self.add_to_memory("l")
        self.robot.movel([x, y, z, rx, ry, rz], vel=self._speed, acc=self._acceleration)

    def move_p(self, x, y, z, rx, ry, rz, add_to_history=False):
        if add_to_history:
            self.add_to_memory("p")
        self.robot.movep([x, y, z, rx, ry, rz], vel=self._speed, acc=self._acceleration)

    def stop(self, home=False):
        if home:
            self.move(*POSES.HOME)
        self.robot.close()

    def interactive_test(self):
        leave = False
        while not leave:
            print("Which operation to use? (j, l, p, q)")
            letter = input_getter(["j", "l", "p", "q"], str)
            if letter == "q":
                break

            print("Which pose entry to add to? (0-5)")
            add_to = input_getter([1, 2, 3, 4, 5], int)
            print("How much to add?")
            to_add = input_getter(None, type_to_convert=float)

            if letter == "j":
                pose = self.robot.getj()
                pose[add_to] += to_add
                self.robot.movej(*pose)
            elif letter == "l":
                pose = self.robot.getl()
                pose[add_to] += to_add
                self.robot.movel(pose)
            elif letter == "p":
                # TODO; verify if this pose works
                pose = self.robot.get_pose()
                pose[add_to] += to_add
                self.robot.movep(pose)



if __name__ == '__main__':
    # try:
    a = Arm(0)
    try:
        # a.move_cartesian(*POSES.ABOVE_PAYLOAD_TCP_POSE_1, add_to_history=True)
        a.robot.getl()
        # a.robot.stopl()
    except Exception as e:
        traceback.print_exc()
    finally:
        a.robot.close()
    # except Exception as e:
    #     print(traceback.print_exc())
    # finally:
    # a.robot.stopj()
