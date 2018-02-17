__author__ = 'Indy'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import socket
import pickle

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

        testbutton = QPushButton('Send Test Signal', self)
        testbutton.setToolTip('Test Signal Button')
        testbutton.move(100,70)
        testbutton.clicked.connect(self.on_testbutton_click)

        self.show()

    @pyqtSlot()
    def on_testbutton_click(self):
        testtup = pickle.dumps((3, 3, 155, 233, 21))
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