# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_FileTree.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_file_manager(object):
    def setupUi(self, file_manager):
        file_manager.setObjectName("file_manager")
        file_manager.resize(715, 586)
        self.gridLayout_2 = QtWidgets.QGridLayout(file_manager)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_path = QtWidgets.QLineEdit(file_manager)
        self.lineEdit_path.setReadOnly(True)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout_2.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QGridLayout()
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_2.addLayout(self.treeWidget, 1, 0, 1, 1)

        self.retranslateUi(file_manager)
        QtCore.QMetaObject.connectSlotsByName(file_manager)

    def retranslateUi(self, file_manager):
        _translate = QtCore.QCoreApplication.translate
        file_manager.setWindowTitle(_translate("file_manager", "Файловый менеджер"))

