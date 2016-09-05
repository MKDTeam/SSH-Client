# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

############################################
import paramiko
import sys
#Подключаем необходимые модули (Основные GUI виджеты находятся в библиотеке QtGui)
app = QtGui.QApplication(sys.argv)
############################################

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    ############################################
    #SSHClient – это основной класс, который нужен чтобы подключаться и работать удаленно. Он дает сессию для дальнейшей работы
    client = paramiko.SSHClient()

    #Функция, содержащая в себе данные необходимые для подлючения
    #self.lineEdit_x.text() содержит данные введенные пользователем
    def refresh_data(self):
        self.host = '192.168.1.42'#self.lineEdit_host.text()
        self.user = 'dmitry'#self.lineEdit_user.text()
        self.password = '123321'#self.lineEdit_password.text()
        self.port = 22#int(self.lineEdit_port.text())

    #Функция, производящая подключение к серверу по полученным данным
    def connect(self):
        self.refresh_data()
        #Добавляем ключ сервера в список известных хостов — файл .ssh/known_hosts
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Соединение с сервером
        self.client.connect(hostname = self.host, username = self.user, password = self.password, port = self.port)

    #Функция, отправляющая команды на сервер
    def send_command(self):
        #Строка client.exec_command() — выполняет команду на удаленном сервере
        #plainTextEdit_input.toPlainText() содержит команду введенную пользователем в UI интерфейсе
        #Потоки ввода-вывода программы возврашщаются в файлообразные обьекты — stdin, stdout, stderr
        #stdin - поток ввода данных
        #stdout - стандартный поток вывода данных
        #stderr - поток вывода ошибок (если программа не смогла сделать все как надо — она пишет  в этот поток)
        stdin, stdout, stderr = self.client.exec_command(self.plainTextEdit_input.toPlainText())
        self.data = stdout.read() + stderr.read()
        #Вывод полученных данных data в UI интерфейс
        #Т.к. данные получаем в виде байтов, необходимо их декодировать с помощью data.decode('utf-8')
        self.plainTextEdit_output.setPlainText(self.data.decode('utf-8'))

    #Функция отключения соединения с сервером
    def disconnect(self):
        self.client.close()
    ############################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(612, 546)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_host = QtGui.QLabel(self.groupBox)
        self.label_host.setObjectName(_fromUtf8("label_host"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_host)
        self.lineEdit_host = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_host)
        self.label_user = QtGui.QLabel(self.groupBox)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_user)
        self.lineEdit_user = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_password = QtGui.QLabel(self.groupBox)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_port = QtGui.QLabel(self.groupBox)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_port.setEnabled(True)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_port)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_output.setObjectName(_fromUtf8("groupBox_output"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_output)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_output = QtGui.QPushButton(self.groupBox_output)
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.gridLayout_2.addWidget(self.pushButton_output, 1, 0, 1, 1)
        self.plainTextEdit_output = QtGui.QPlainTextEdit(self.groupBox_output)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setObjectName(_fromUtf8("plainTextEdit_output"))
        self.gridLayout_2.addWidget(self.plainTextEdit_output, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_output, 7, 0, 1, 1)
        self.groupBox_input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName(_fromUtf8("groupBox_input"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_input)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit_input = QtGui.QPlainTextEdit(self.groupBox_input)
        self.plainTextEdit_input.setPlainText(_fromUtf8(""))
        self.plainTextEdit_input.setObjectName(_fromUtf8("plainTextEdit_input"))
        self.gridLayout.addWidget(self.plainTextEdit_input, 2, 0, 1, 1)
        self.pushButton_input = QtGui.QPushButton(self.groupBox_input)
        self.pushButton_input.setObjectName(_fromUtf8("pushButton_input"))
        self.gridLayout.addWidget(self.pushButton_input, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_input, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_connect = QtGui.QPushButton(self.centralwidget)
        self.pushButton_connect.setEnabled(True)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.horizontalLayout.addWidget(self.pushButton_connect)
        self.pushButton_disconnect = QtGui.QPushButton(self.centralwidget)
        self.pushButton_disconnect.setObjectName(_fromUtf8("pushButton_disconnect"))
        self.horizontalLayout.addWidget(self.pushButton_disconnect)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect)
        QtCore.QObject.connect(self.pushButton_output, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit_output.clear)
        QtCore.QObject.connect(self.pushButton_disconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.disconnect)
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_command)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Клиент", None))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры подключения", None))
        self.label_host.setText(_translate("MainWindow", "Хост", None))
        self.label_user.setText(_translate("MainWindow", "Имя пользователя", None))
        self.label_password.setText(_translate("MainWindow", "Пароль", None))
        self.label_port.setText(_translate("MainWindow", "Порт", None))
        self.groupBox_output.setTitle(_translate("MainWindow", "Вывод", None))
        self.pushButton_output.setText(_translate("MainWindow", "Очистить вывод", None))
        self.groupBox_input.setTitle(_translate("MainWindow", "Консоль ввода команд", None))
        self.pushButton_input.setText(_translate("MainWindow", "Отправить команду", None))
        self.pushButton_connect.setText(_translate("MainWindow", "Подключится", None))
        self.pushButton_disconnect.setText(_translate("MainWindow", "Отключится", None))

############################################
#Запуск главного окна приложения
window = QtGui.QMainWindow()
content = Ui_MainWindow()
content.setupUi(window)
window.show()

sys.exit(app.exec_())
############################################