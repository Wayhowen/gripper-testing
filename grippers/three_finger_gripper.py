import time

from grippers.gripper_base import Gripper
from utils.bluetooth import Bluetooth


class ThreeFingerGripper(Gripper):
    def __init__(self, height, width, length):
        super().__init__(height, width, length)
        self.gripper_receiver = Bluetooth(mac='00:18:e4:34:d4:18', port=1)

    def open(self):
        self.gripper_receiver.send(0)

    def close(self):
        self.gripper_receiver.send(200)


if __name__ == '__main__':
    gripper = ThreeFingerGripper(0, 0, 0)
    gripper.open()
    time.sleep(3)
    gripper.close()
    time.sleep(3)