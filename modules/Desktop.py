from  modules.ui_class.ui_Desktop import Ui_MainWindow
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import QObject, QUrl, pyqtSlot


class Desktop(Ui_MainWindow, QObject):
    """В этом классе осуществляется управление рабочей областью программы"""
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self.window)
        self.declarativeView.setSource(QUrl('modules/Desktop_workspace.qml'))
        self.qml_descktop = self.declarativeView.rootObject()
        self.declarativeView.engine().rootContext().setContextObject(self)
        self.declarativeView.resizeEvent = lambda resizeEvent: self.qml_descktop.resize_workspace(resizeEvent.size().width(), resizeEvent.size().height()) # связка размеров окна и рабочей области

        self.qml_descktop.run_terminal.connect(self.start_terminal)
        self.action_terminal.triggered.connect(self.start_terminal)
        self.qml_descktop.run_file_manager.connect(self.start_file_manager)
        self.action_file_manager.triggered.connect(self.start_file_manager)

        self.application_list = {}

    @pyqtSlot(str)
    def show_status(self, text):
        #print(text)
        self.statusbar.showMessage(text)

    def start(self):
        self.window.show()

    def start_terminal(self, function = None):
        if function:
            self.application_list['terminal'] = function
            return
        if 'terminal' in self.application_list:
            self.application_list['terminal']()
        else:
            print('Приложения "terminal" не существует')

    def start_file_manager(self, function = None):
        if function:
            self.application_list['file_manager'] = function
            return
        if 'file_manager' in self.application_list:
            self.application_list['file_manager']()
        else:
            print('Приложения "file_manager" не существует')


#import sys
#app = QtGui.QApplication(sys.argv)
#
#client = Desktop()
#client.show()
#
#sys.exit(app.exec_())