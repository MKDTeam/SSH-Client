# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(302, 589)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_options = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_options.sizePolicy().hasHeightForWidth())
        self.groupBox_options.setSizePolicy(sizePolicy)
        self.groupBox_options.setAutoFillBackground(True)
        self.groupBox_options.setObjectName(_fromUtf8("groupBox_options"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_options)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_host = QtGui.QLabel(self.groupBox_options)
        self.label_host.setObjectName(_fromUtf8("label_host"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_host)
        self.lineEdit_host = QtGui.QLineEdit(self.groupBox_options)
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_host)
        self.label_user = QtGui.QLabel(self.groupBox_options)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_user)
        self.lineEdit_user = QtGui.QLineEdit(self.groupBox_options)
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_password = QtGui.QLabel(self.groupBox_options)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtGui.QLineEdit(self.groupBox_options)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_port = QtGui.QLabel(self.groupBox_options)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtGui.QLineEdit(self.groupBox_options)
        self.lineEdit_port.setEnabled(True)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_port)
        self.gridLayout_3.addWidget(self.groupBox_options, 0, 0, 1, 1)
        self.groupBox_output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_output.setAutoFillBackground(True)
        self.groupBox_output.setObjectName(_fromUtf8("groupBox_output"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_output)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_output = QtGui.QPushButton(self.groupBox_output)
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.gridLayout_2.addWidget(self.pushButton_output, 1, 0, 1, 1)
        self.plainTextEdit_output = QtGui.QPlainTextEdit(self.groupBox_output)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_output.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_output.setSizePolicy(sizePolicy)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setObjectName(_fromUtf8("plainTextEdit_output"))
        self.gridLayout_2.addWidget(self.plainTextEdit_output, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_output, 7, 0, 1, 1)
        self.groupBox_input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_input.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_input.setAutoFillBackground(True)
        self.groupBox_input.setObjectName(_fromUtf8("groupBox_input"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_input)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit_input = QtGui.QPlainTextEdit(self.groupBox_input)
        self.plainTextEdit_input.setMinimumSize(QtCore.QSize(0, 30))
        self.plainTextEdit_input.setObjectName(_fromUtf8("plainTextEdit_input"))
        self.gridLayout.addWidget(self.plainTextEdit_input, 2, 0, 1, 1)
        self.pushButton_input = QtGui.QPushButton(self.groupBox_input)
        self.pushButton_input.setObjectName(_fromUtf8("pushButton_input"))
        self.gridLayout.addWidget(self.pushButton_input, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_input, 6, 0, 1, 1)
        self.horizontalLayout_options = QtGui.QHBoxLayout()
        self.horizontalLayout_options.setObjectName(_fromUtf8("horizontalLayout_options"))
        self.pushButton_connect = QtGui.QPushButton(self.centralwidget)
        self.pushButton_connect.setEnabled(True)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.horizontalLayout_options.addWidget(self.pushButton_connect)
        self.pushButton_disconnect = QtGui.QPushButton(self.centralwidget)
        self.pushButton_disconnect.setObjectName(_fromUtf8("pushButton_disconnect"))
        self.horizontalLayout_options.addWidget(self.pushButton_disconnect)
        self.gridLayout_3.addLayout(self.horizontalLayout_options, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_output, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit_output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Клиент", None))
        self.groupBox_options.setTitle(_translate("MainWindow", "Параметры подключения", None))
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
