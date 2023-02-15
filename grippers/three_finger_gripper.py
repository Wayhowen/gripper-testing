import time

from grippers.gripper_base import Gripper
from utils.bluetooth.pybluez import Bluetooth


class ThreeFingerGripper(Gripper):
    def __init__(self, height, width, length, weight):
        super().__init__(height, width, length, weight, arm_connected=False)
        self.gripper_receiver = Bluetooth(mac='00:18:e4:34:d4:18', port=1)
        self.open()

    def open(self):
        self.gripper_receiver.send(0)
        self._gripper_state = "open"

    def close(self):
        self.gripper_receiver.send(200)
        self._gripper_state = "closed"


if __name__ == '__main__':
    gripper = ThreeFingerGripper(0, 0, 0, 0.150)

    while True:
        print("waiting for command")
        inp = input()
        if inp == "1":
            gripper.open()
        elif inp == "2":
            gripper.close()
        else:
            print(f"breaking on inp {inp} of type {type(inp)}")
            break