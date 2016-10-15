import sys
from PyQt5.QtWidgets import QApplication

application = QApplication(sys.argv)

from modules.Connection import Settings, ConnectionManager
from modules.Console import Console
from modules.Desktop import Desktop
from modules.FileTree import FileManager

current_settings = Settings('settings.xml')
connection_manager = ConnectionManager()
file_manager = FileManager()
desktop = Desktop()
console = Console()

connection_manager.set_buttons_events(button_load_func = lambda: connection_manager.load_settings(current_settings),
                                      button_connect_func = lambda: connection_manager.connect(),
                                      button_exit_func  = lambda: application.exit())

desktop.add_application(name = 'terminal',
						function = lambda: console.start(connection_manager.client))

desktop.add_application(name = 'file_manager',
						function = lambda: file_manager.start(connection_manager.client))

connection_manager.signalOnConnect.connect(desktop.show)
connection_manager.signalOnConnect.connect(connection_manager.hide)
connection_manager.show()

sys.exit(application.exec_())