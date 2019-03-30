import io
import sys
import socket
import struct
import time 
import pickle
import cv2 as cv
import numpy as np

class Server():
    def __init__(self, ip, port= 8080):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.payload_size = struct.calcsize(">L")

    def build_socket(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        conn, addr = self.server_socket.accept()
        self.conn = conn

    def close_socket(self):
        self.server_socket.close()

    def receive_image(self):
        data = b""
        while len(data) < self.payload_size:
            data += self.conn.recv(4096)
        packed_msg_size = data[:self.payload_size]
        data = data[self.payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += self.conn.recv(4096)
        img_data = data[:msg_size]
        img_data = pickle.loads(img_data, fix_imports= True, encoding= "bytes")
        img = cv.imdecode(img_data, cv.IMREAD_COLOR)
        return img

class Client():
    def __init__(self, server_ip, port= 8080):
        self.server_ip = server_ip
        self.port = port
        self.encode_param = [int(cv.IMWRITE_JPEG_QUALITY), 90]
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def build_socket(self): 
        self.client_socket.connect((self.server_ip, self.port))

    def close_socket(self):
        self.client_socket.close()

    def send_image(self, img):
        result, img = cv.imencode('.jpg', img, self.encode_param)
        data = pickle.dumps(img, 0)
        size = len(data)
        self.client_socket.sendall(struct.pack(">L", size) + data)

def test_server():
    ip = '10.10.2.99'
    server = Server(ip)
    server.build_socket()
    img = server.receive_image()
    cv.imshow('server', img)
    cv.waitKey(0)


def test_client():
    ip = '10.10.2.99'
    client = Client(ip)
    img = cv.imread('test/lena.jpg')
    client.build_socket()
    client.send_image(img)
    client.close_socket()

if __name__ == '__main__':
    print('- transfer -')
    test_client()