import sys
import os.path as path
import clipboard
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QToolBar, QAction, qApp, QMainWindow
from PyQt5.QtGui import QIcon
from test import Ui_MainWindow


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.init_ui()


        # buttons-actions
        self.ui.clip_btn.clicked.connect(self.clip_paste)

    def init_ui(self):
        self.setWindowTitle("strm sender")
        self.setWindowIcon(QIcon('./assets/kodi.png'))
        



        # actions
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        sendAct = QAction(QIcon('send.png'), 'Send', self)
        sendAct.setShortcut('Ctrl+X')
        sendAct.triggered.connect(self.send_test)
 
        # toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(sendAct)

    def send_test(self):
        print("action sended")

    def clip_paste(self): #  pastes from the clipboard
        text = clipboard.paste()
        self.ui.url_line_edit.setText(text)
        self.send(text)


    def send(self, text):
        with open('./ip.log', 'r') as f: #  opens the ip extension file
            ip_ext = f.read()
        ip = '192.168.1.' + ip_ext
        url = text
        print(url)
        kodi_path = '\\\\' + ip
        file_path = kodi_path + '\\berryboot\\New Folder\\test.strm'

        with open(file_path, 'w') as f:
            f.write(url)

        self.ui.url_line_edit.clear()










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

