# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_FileTree.ui'
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

class Ui_file_manager(object):
    def setupUi(self, file_manager):
        file_manager.setObjectName(_fromUtf8("file_manager"))
        file_manager.resize(715, 586)
        self.gridLayout_2 = QtGui.QGridLayout(file_manager)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_path = QtGui.QLineEdit(file_manager)
        self.lineEdit_path.setReadOnly(True)
        self.lineEdit_path.setObjectName(_fromUtf8("lineEdit_path"))
        self.gridLayout_2.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.treeWidget = QtGui.QGridLayout()
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout_2.addLayout(self.treeWidget, 1, 0, 1, 1)

        self.retranslateUi(file_manager)
        QtCore.QMetaObject.connectSlotsByName(file_manager)

    def retranslateUi(self, file_manager):
        file_manager.setWindowTitle(_translate("file_manager", "Файловый менеджер", None))

