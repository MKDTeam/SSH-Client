from modules.ui_class.ui_Desktop import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, QUrl, pyqtSlot


class Desktop(Ui_MainWindow, QObject):
    """В этом классе осуществляется управление рабочей областью программы"""
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self.window)
        self.quickWidget.setSource(QUrl('modules/Desktop_workspace.qml'))
        self.qml_descktop = self.quickWidget.rootObject()
        self.quickWidget.engine().rootContext().setContextObject(self)
        self.quickWidget.resizeEvent = lambda resizeEvent: self.qml_descktop.resize_workspace(resizeEvent.size().width(), resizeEvent.size().height()) # связка размеров окна и рабочей области

        self.action_terminal.triggered.connect(lambda: self.start_application('terminal'))
        self.action_file_manager.triggered.connect(lambda: self.start_application('file_manager'))

        self.application_list = {}

    @pyqtSlot(str) # Изменение текста статус бара
    def show_status(self, text):
        self.statusbar.showMessage(text)

    @pyqtSlot(str)
    def start_application(self, name):
        if name in self.application_list:
            self.application_list[name]()

    def show(self):
        self.window.show()

    def add_application(self, name, function):
        if name and function:
            self.application_list[name] = function
        else:
            print('Ошибка в аргументах функции "Desktop.add_application()"')