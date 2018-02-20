import socketserver
import json
import unicornhat as uni
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
            self.radar_signal(s['data'])
        #self.play(s['data'])

    def play(self, pixels):
        pass

    def radar_signal(self, pixels):
        """
        This is the broadcast handler from the Animation GUI to advise if a server has been found and
        if it is a SD or HD hat
        :param pixels:
        :return:
        """

        # Show a test connection light for the pi
        uni.set_pixel(pixels[0], pixels[1], pixels[2], pixels[3], pixels[4])
        uni.show()
        time.sleep(2)
        uni.set_pixel(pixels[0], pixels[1], 0,0,0)
        uni.show()

        # Send back confirmation of the ip address and the type of hat
        with open('server.json') as server_json:
            server_config = json.load(server_json)
            self.request.sendall(bytes(server_config, 'utf-8'))


if __name__ == '__main__':

    HOST, PORT = '192.168.0.40', 9999

    server = socketserver.TCPServer((HOST, PORT), AnimatorServer)

    server.serve_forever()

