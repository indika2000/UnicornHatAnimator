import socketserver
import socket
import pickle
import json
#import unicornhat as uni
import time

class AnimatorServer(socketserver.BaseRequestHandler):
    """
    The Main server for the animator GUI

    It will check for:
        1) All Unicorn HATs listening for the server
        2) Be able to send animations to the respective RPi and their HATs
    """
    def handle(self):
        jam = str(self.request.recv(1024).strip(), 'utf-8')
        s = json.loads(jam)
        print("Received GUI Action {0} ".format(s['action']))
        if s['action'] == 'test':
            self.test_signal(s['data'])
        #self.play(s['data'])

    def play(self, pixels):
        pass

    def test_signal(self, pixels):
        uni.set_pixel(pixels[0], pixels[1], pixels[2], pixels[3], pixels[4])
        uni.show()
        time.sleep(10)
        uni.set_pixel(pixels[0], pixels[1], 0,0,0)
        uni.show()

if __name__ == '__main__':

    a = 10
    if a == 10:
        import unicornhat as uni

    HOST, PORT = '192.168.0.40', 9999

    server = socketserver.TCPServer((HOST, PORT), AnimatorServer)

    server.serve_forever()

