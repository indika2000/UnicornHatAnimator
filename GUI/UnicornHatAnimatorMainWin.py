__author__ = 'Indy'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import socket
import time

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #find all connecting machines
        try:
            self.is_anybody_out_there()
        except:
            pass

        testbutton = QPushButton('Send Test Signal', self)
        testbutton.setToolTip('Test Signal Button')
        testbutton.move(100,70)
        testbutton.clicked.connect(self.on_testbutton_click)

        self.show()

    #Signal to find all listening HATs
    def is_anybody_out_there(self):
        for e in range(39, 42):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                ip = "192.168.0.{}".format(e)
                print('Attempting to connect to {}'.format(ip))
                sock.settimeout(0.1)
                try:
                    testjson = '{ "action": "test", "data": [3, 3, 155, 233, 21] }'
                    sock.connect((ip, 9999))
                    sock.sendall(bytes(testjson + '\n', 'utf-8'))
                    print('Rec data before')
                    data_reply = str(sock.recv(1024), 'utf-8')
                    print('Rec data after')
                    print(data_reply)
                except OSError as msg:
                    print('Here!! {}'.format(msg))
                    sock.close()
                except:
                    print('some else is wrong')



    @pyqtSlot()
    def on_testbutton_click(self):
        testjson = '{ "action": "test", "data": [3, 3, 155, 233, 21] }'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("192.168.0.40", 9999))
            print(testjson)
            try:
                sock.sendall(bytes(testjson + '\n', 'utf-8'))
            except:
                pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())