# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Desktop.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.gridLayout.addWidget(self.quickWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        self.tools = QtWidgets.QMenu(self.menubar)
        self.tools.setObjectName("tools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new_connection = QtWidgets.QAction(MainWindow)
        self.action_new_connection.setObjectName("action_new_connection")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_terminal = QtWidgets.QAction(MainWindow)
        self.action_terminal.setObjectName("action_terminal")
        self.action_file_manager = QtWidgets.QAction(MainWindow)
        self.action_file_manager.setObjectName("action_file_manager")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Менеджер удаленного управления сервером"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.help.setTitle(_translate("MainWindow", "Справка"))
        self.tools.setTitle(_translate("MainWindow", "Инструменты"))
        self.action_new_connection.setText(_translate("MainWindow", "Новое соединение"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_terminal.setText(_translate("MainWindow", "Удаленный терминал"))
        self.action_file_manager.setText(_translate("MainWindow", "Файловый менеджер"))
        self.action_settings.setText(_translate("MainWindow", "Настройки"))

from PyQt5 import QtQuickWidgets
