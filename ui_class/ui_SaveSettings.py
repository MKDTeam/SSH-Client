# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_SaveSettings.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qDialog_save(object):
    def setupUi(self, qDialog_save):
        qDialog_save.setObjectName("qDialog_save")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qDialog_save.sizePolicy().hasHeightForWidth())
        qDialog_save.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(qDialog_save)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(qDialog_save)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.label_subtitle = QtWidgets.QLabel(qDialog_save)
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout_2.addWidget(self.label_subtitle)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.pushButton_yes = QtWidgets.QPushButton(qDialog_save)
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.horizontalLayout_1.addWidget(self.pushButton_yes)
        self.pushButton_no = QtWidgets.QPushButton(qDialog_save)
        self.pushButton_no.setObjectName("pushButton_no")
        self.horizontalLayout_1.addWidget(self.pushButton_no)
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)
        self.groupBox = QtWidgets.QGroupBox(qDialog_save)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.groupBox)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_confirm = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.verticalLayout.addWidget(self.pushButton_confirm)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(qDialog_save)
        self.pushButton_yes.clicked.connect(self.groupBox.show)
        self.pushButton_yes.clicked['bool'].connect(self.pushButton_yes.setEnabled)
        self.pushButton_no.clicked.connect(qDialog_save.close)
        self.pushButton_yes.clicked.connect(self.lineEdit_password.setFocus)
        QtCore.QMetaObject.connectSlotsByName(qDialog_save)

    def retranslateUi(self, qDialog_save):
        _translate = QtCore.QCoreApplication.translate
        qDialog_save.setWindowTitle(_translate("qDialog_save", "Dialog"))
        self.label_title.setText(_translate("qDialog_save", "Создан новый набор настроек."))
        self.label_subtitle.setText(_translate("qDialog_save", "Желаете сохранить их?"))
        self.pushButton_yes.setText(_translate("qDialog_save", "Да"))
        self.pushButton_no.setText(_translate("qDialog_save", "Нет"))
        self.label_password.setText(_translate("qDialog_save", "Пароль"))
        self.lineEdit_password.setPlaceholderText(_translate("qDialog_save", " Введите новый пароль"))
        self.pushButton_confirm.setText(_translate("qDialog_save", "Потвердить"))

