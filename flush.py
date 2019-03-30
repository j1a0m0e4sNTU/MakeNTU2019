import socket 
from button import Button
import RPi.GPIO as GPIO

class Flusher():
    def __init__(self, server_ip= '10.10.3.21', port= 8080):
        GPIO.setmode(GPIO.BCM)
        self.server_socket = socket.socket(socket.AF_INET)
        self.server_socket.bind((server_ip, port))
        self.server_socket.listen(5)
        self.flush = False
        def call_back(channel):
            self.flush = True
        self.button = Button(4, call_back)

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            while True:
                if self.flush:
                    break     
            
            conn.send(b'1')
            conn.close()
            self.flush = False

if __name__ == '__main__':
    flusher = Flusher()
    print('Run ...')
    flusher.run()