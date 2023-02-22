import time

import bluetooth


class Bluetooth:
    def __init__(self, mac='20:16:03:10:03:48', port=1):
        self._socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self._socket.connect((mac, port))

    def send(self, data):
        self._socket.send(bytes(str(data), 'UTF-8'))
        self.wait_until_received(data)

    def close_connection(self):
        self._socket.close()

    # TODO: if we figure out how to do bluetooth send/receive, change this
    def wait_until_received(self, data):
        if data == 0:
            time.sleep(2)
        else:
            time.sleep(4)

if __name__ == '__main__':
    # simple inquiry example
    b = Bluetooth()
    while True:
        b.send(input())
    # time.sleep(2)
    # b.send(256)
    # time.sleep(2)
    # b.close_connection()
