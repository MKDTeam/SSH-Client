#from PyQt5.QtWidgets import QMainWindow 
import sys, os
from PyQt5.QtCore import QObject, QTimer, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

application = QApplication(sys.argv)

from Connection import Settings, ConnectionManager
from Desktop import Desktop

connection_manager = ConnectionManager()
connection_manager.setButtonsEvents(button_connect_func = lambda: connection_manager.connect(),
                                    button_exit_func  = lambda: application.exit())

#"folderView.qml"engine = QQmlApplicationEngine("ApplicationWindow.qml")
engine = QQmlApplicationEngine("Application.qml")
desktop = Desktop(engine, connection_manager.client, connection_manager.settings)

connection_manager.signal_onConnect.connect(desktop.start)
connection_manager.signal_onConnect.connect(connection_manager.hide)
connection_manager.show()


sys.exit(application.exec_())

#ls /usr/share/terminfo/*
#JSON.parse(JSON.stringify(model.fileURL))

#find . -type f -maxdepth 1 -perm -o+r -exec md5 {} + | sed 's/MD5 (//;s/)//'