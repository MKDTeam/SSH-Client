# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Desktop.ui'
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
        MainWindow.resize(829, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.declarativeView = QtDeclarative.QDeclarativeView(self.centralwidget)
        self.declarativeView.setObjectName(_fromUtf8("declarativeView"))
        self.gridLayout.addWidget(self.declarativeView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.help = QtGui.QMenu(self.menubar)
        self.help.setObjectName(_fromUtf8("help"))
        self.tools = QtGui.QMenu(self.menubar)
        self.tools.setObjectName(_fromUtf8("tools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_new_connection = QtGui.QAction(MainWindow)
        self.action_new_connection.setObjectName(_fromUtf8("action_new_connection"))
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_terminal = QtGui.QAction(MainWindow)
        self.action_terminal.setObjectName(_fromUtf8("action_terminal"))
        self.action_file_manager = QtGui.QAction(MainWindow)
        self.action_file_manager.setObjectName(_fromUtf8("action_file_manager"))
        self.action_settings = QtGui.QAction(MainWindow)
        self.action_settings.setObjectName(_fromUtf8("action_settings"))
        self.menu.addAction(self.action_new_connection)
        self.menu.addAction(self.action_settings)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.tools.addAction(self.action_terminal)
        self.tools.addAction(self.action_file_manager)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Менеджер удаленного управления сервером", None))
        self.menu.setTitle(_translate("MainWindow", "Меню", None))
        self.help.setTitle(_translate("MainWindow", "Справка", None))
        self.tools.setTitle(_translate("MainWindow", "Инструменты", None))
        self.action_new_connection.setText(_translate("MainWindow", "Новое соединение", None))
        self.action_exit.setText(_translate("MainWindow", "Выход", None))
        self.action_terminal.setText(_translate("MainWindow", "Удаленный терминал", None))
        self.action_file_manager.setText(_translate("MainWindow", "Файловый менеджер", None))
        self.action_settings.setText(_translate("MainWindow", "Настройки", None))

from PyQt4 import QtDeclarative
