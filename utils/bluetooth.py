import socket
import time


class Bluetooth:
    def __init__(self, mac='00:18:e4:34:d4:18', port=1):
        self._socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self._socket.connect((mac, port))
        time.sleep(3)

    def send(self, data):
        self._socket.send(bytes(str(data), 'UTF-8'))

    def close_connection(self):
        self._socket.close()
