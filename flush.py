import socket 
from button import Button

class Flusher():
    def __init__(self, server_ip= '10.10.3.21', port= 8080):
        self.socket = socket.socket(socket.AF_INET)
        self.socket.bind((server_ip, port))
        self.socket.listen(5)
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

    def __del__(self):
        self.socket.close()
