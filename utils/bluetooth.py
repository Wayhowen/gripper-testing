import socket
import time


class Bluetooth:
    def __init__(self, mac='00:18:e4:34:d4:18', port=1):
        self._socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self._socket.connect((mac, port))

    def send(self, data):
        self._socket.send(bytes(str(data), 'UTF-8'))
        self.wait_until_received()

    def close_connection(self):
        self._socket.close()
        self.wait_until_received()

    # TODO: if we figure out how to do bluetooth send/receive, change this
    def wait_until_received(self):
        time.sleep(1)
