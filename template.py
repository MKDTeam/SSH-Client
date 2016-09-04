
""" Тест работы QT
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())
"""

##########################################################

""" Тест работы paramiko
import paramiko 

host = '192.168.1.42'
user = 'dmitry'
secret = '123321'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
#stdin, stdout, stderr = client.exec_command('ls /')
stdin, stdout, stderr = client.exec_command('cd /home/')
data = stdout.read() + b"--------------------------------------\n" + stderr.read()
client.close()

my_file = open("log.txt", "w")
my_file.write(data.decode('utf-8'))
"""

##########################################################

""" Тест работы формы
import sys

app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
content = Ui_MainWindow()
content.setupUi(window)
window.show()

sys.exit(app.exec_())
"""

##########################################################

""" Работа с формой
import paramiko
import sys
app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
content = Ui_MainWindow()
content.setupUi(window)
window.show()

class SSH_Client(object):
    host = content.lineEdit_host.text
    user = content.lineEdit_user.text
    password = content.lineEdit_password.text
    port = content.lineEdit_port.text

    client = paramiko.SSHClient()

    def refresh_data(self):
        host = content.lineEdit_host.text
        user = content.lineEdit_user.text
        password = content.lineEdit_password.text
        port = content.lineEdit_port.text

    def connect(self):
        self.refresh_data(self)
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname = self.host, username = self.user, password = self.password, port = self.port)
    
    def send_command(self, command):
        stdin, stdout, stderr = client.exec_command(command)
        self.data = stdout.read() + stderr.read()


    def disconnect(self):
        self.client.close()

sys.exit(app.exec_())
"""