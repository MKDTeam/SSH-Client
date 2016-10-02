# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Connection.ui'
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

class Ui_Dialog_connection(object):
    def setupUi(self, Dialog_connection):
        Dialog_connection.setObjectName(_fromUtf8("Dialog_connection"))
        Dialog_connection.resize(513, 191)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_connection)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget_options = QtGui.QTabWidget(Dialog_connection)
        self.tabWidget_options.setObjectName(_fromUtf8("tabWidget_options"))
        self.widget_main_options = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main_options.sizePolicy().hasHeightForWidth())
        self.widget_main_options.setSizePolicy(sizePolicy)
        self.widget_main_options.setObjectName(_fromUtf8("widget_main_options"))
        self.formLayout_3 = QtGui.QFormLayout(self.widget_main_options)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_host = QtGui.QLabel(self.widget_main_options)
        self.label_host.setObjectName(_fromUtf8("label_host"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_host)
        self.lineEdit_host = QtGui.QLineEdit(self.widget_main_options)
        self.lineEdit_host.setText(_fromUtf8(""))
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_host)
        self.label_user = QtGui.QLabel(self.widget_main_options)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_user)
        self.lineEdit_user = QtGui.QLineEdit(self.widget_main_options)
        self.lineEdit_user.setText(_fromUtf8(""))
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_secret = QtGui.QLabel(self.widget_main_options)
        self.label_secret.setObjectName(_fromUtf8("label_secret"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_secret)
        self.lineEdit_secret = QtGui.QLineEdit(self.widget_main_options)
        self.lineEdit_secret.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_secret.setObjectName(_fromUtf8("lineEdit_secret"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_secret)
        self.tabWidget_options.addTab(self.widget_main_options, _fromUtf8(""))
        self.widget_additional_options = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_additional_options.sizePolicy().hasHeightForWidth())
        self.widget_additional_options.setSizePolicy(sizePolicy)
        self.widget_additional_options.setObjectName(_fromUtf8("widget_additional_options"))
        self.formLayout_4 = QtGui.QFormLayout(self.widget_additional_options)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_port = QtGui.QLabel(self.widget_additional_options)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtGui.QLineEdit(self.widget_additional_options)
        self.lineEdit_port.setText(_fromUtf8("22"))
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_port)
        self.label_terminal_type = QtGui.QLabel(self.widget_additional_options)
        self.label_terminal_type.setObjectName(_fromUtf8("label_terminal_type"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_terminal_type)
        self.lineEdit_terminal_type = QtGui.QLineEdit(self.widget_additional_options)
        self.lineEdit_terminal_type.setText(_fromUtf8("xfce4-terminal"))
        self.lineEdit_terminal_type.setObjectName(_fromUtf8("lineEdit_terminal_type"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_terminal_type)
        self.tabWidget_options.addTab(self.widget_additional_options, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget_options)
        self.horizontalLayout_buttons = QtGui.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(_fromUtf8("horizontalLayout_buttons"))
        self.pushButton_load = QtGui.QPushButton(Dialog_connection)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout_buttons.addWidget(self.pushButton_load)
        self.pushButton_connect = QtGui.QPushButton(Dialog_connection)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.horizontalLayout_buttons.addWidget(self.pushButton_connect)
        self.pushButton_exit = QtGui.QPushButton(Dialog_connection)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.horizontalLayout_buttons.addWidget(self.pushButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        self.retranslateUi(Dialog_connection)
        self.tabWidget_options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_connection)

    def retranslateUi(self, Dialog_connection):
        Dialog_connection.setWindowTitle(_translate("Dialog_connection", "Dialog", None))
        self.label_host.setText(_translate("Dialog_connection", "Адрес хоста", None))
        self.label_user.setText(_translate("Dialog_connection", "Имя пользователя", None))
        self.label_secret.setText(_translate("Dialog_connection", "Пароль", None))
        self.tabWidget_options.setTabText(self.tabWidget_options.indexOf(self.widget_main_options), _translate("Dialog_connection", "Параметры соеденения", None))
        self.label_port.setText(_translate("Dialog_connection", "Порт", None))
        self.label_terminal_type.setText(_translate("Dialog_connection", "Тип терминала", None))
        self.tabWidget_options.setTabText(self.tabWidget_options.indexOf(self.widget_additional_options), _translate("Dialog_connection", "Дополнительные параметры", None))
        self.pushButton_load.setText(_translate("Dialog_connection", "Загрузить настройки из файла", None))
        self.pushButton_connect.setText(_translate("Dialog_connection", "Подключиться", None))
        self.pushButton_exit.setText(_translate("Dialog_connection", "Выход", None))

