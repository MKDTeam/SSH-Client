import sys
import paramiko
from PyQt4 import QtCore, QtGui
from ui_main_form import Ui_MainWindow

app = QtGui.QApplication(sys.argv)

class SSH_Client(Ui_MainWindow):
    """Расширяет функционал формы, добавляя обработку событий"""
    def __init__(self):
        #super(SSH_Client, self).__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.window = QtGui.QMainWindow()
        self.setupUi(self.window)
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL("clicked()"), self.connect)
        QtCore.QObject.connect(self.pushButton_disconnect, QtCore.SIGNAL("clicked()"), self.disconnect)
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), self.send_command)
        self.window.show()

    def load_data(self):
        self.host = '192.168.1.42'#self.lineEdit_host.text()
        self.user = 'dmitry'#self.lineEdit_user.text()
        self.password = '123321'#self.lineEdit_password.text()
        self.port = 22#int(self.lineEdit_port.text())

    def connect(self):
        self.load_data()
        self.client.connect(hostname = self.host, username = self.user, password = self.password, port = self.port)
    
    def send_command(self):
        stdin, stdout, stderr = self.client.exec_command(self.plainTextEdit_input.toPlainText())
        data = stdout.read() + stderr.read()
        self.plainTextEdit_output.setPlainText(data.decode('utf-8'))

    def disconnect(self):
        self.client.close()

client = SSH_Client()
sys.exit(app.exec_())