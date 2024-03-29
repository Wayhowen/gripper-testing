from grippers.gripper_base import Gripper
from utils.bluetooth.pybluez import Bluetooth


class BraidedGripper(Gripper):
    def __init__(self, height, width, length, weight, bluetooth_connected=True):
        super().__init__(height, width, length, weight)
        self.gripper_receiver = Bluetooth(mac='20:16:03:10:03:48', port=1) if bluetooth_connected else None
        self.open(6)

    def open(self, wait_for: int = 4):
        print("open called")
        if self.gripper_receiver:
            self.gripper_receiver.send(0, wait_for)
            self._gripper_state = "open"

    def close(self, wait_for: int = 4):
        print("close called")
        if self.gripper_receiver:
            self.gripper_receiver.send(1, wait_for)
            self._gripper_state = "closed"


if __name__ == '__main__':
    gripper = BraidedGripper(0, 0, 0, 0.150)

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
