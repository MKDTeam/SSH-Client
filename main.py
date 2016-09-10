import sys
import paramiko
from PyQt4 import QtCore, QtGui
from ui_main_form import Ui_MainWindow
from ui_file_manager import Ui_file_manager
from file_tree_widget import FileTreeWidget

app = QtGui.QApplication(sys.argv)


class Main_Windows():
    """Основное окно программы"""

class SSHClient(Ui_MainWindow):
    """Расширяет функционал формы, добавляя обработку событий"""
    def __init__(self):
        super().__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.window = QtGui.QMainWindow()
        self.setupUi(self.window)
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL("clicked()"), self.connect)
        QtCore.QObject.connect(self.pushButton_disconnect, QtCore.SIGNAL("clicked()"), self.disconnect)
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), self.send_command)
        self.window.show()

    def load_data(self):
        self.host = '192.168.1.42'#self.lineEdit_host.text()
        self.user = 'dmitry'#self.lineEdit_user.text()
        self.password = '123321'#self.lineEdit_password.text()
        self.port = 22#int(self.lineEdit_port.text())

    def connect(self):
        self.load_data()
        self.client.connect(hostname = self.host, username = self.user, password = self.password, port = self.port)
    
    def send_command(self):
        stdin, stdout, stderr = self.client.exec_command(self.plainTextEdit_input.toPlainText())
        data = stdout.read() + stderr.read()
        self.plainTextEdit_output.setPlainText(data.decode('utf-8'))

    def disconnect(self):
        self.client.close()

client = SSHClient()

class FileManager(Ui_file_manager):
    """Графический менеджер работы с файлами"""
    def __init__(self):
        super().__init__()
        #######################################################################
        host = '192.168.1.42'
        user = 'dmitry'
        secret = '123321'
        port = 22

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, username=user, password=secret, port=port)
        stdin, stdout, stderr = self.client.exec_command('ls /')
        data = stdout.read().decode('utf-8')

        self.array = data.split()

        #self.client.close()
        #######################################################################

        self.window = QtGui.QWidget()
        self.setupUi(self.window)

        self.file_tree = FileTreeWidget()
        self.file_tree.setSeparator('/')
        self.file_tree.setHeaderLabels(['Имя файла', 'Тип файла'])
        self.file_tree.header().setResizeMode(3)
        self.file_tree.setSortingEnabled(True)
        self.file_tree.setExpandsOnDoubleClick(False)

        self.treeWidget.addWidget(self.file_tree)

        self.file_tree.newTreeBranch('/', self.getListOfDirectory('/'))
        self.file_tree.topLevelItem(0).setExpanded(True)

        QtCore.QObject.connect(self.file_tree , QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self.treeItemActivated)
        self.window.show()

    def getListOfDirectory(self, path):
        """Возращает список файлов по заданому пути"""
        stdin, stdout, stderr = self.client.exec_command('ls -aF ' + path)
        data = stdout.read().decode('utf-8')
        array = data.split('\n')
        array = array[2:-1]
        return array

    def treeItemActivated(self, tree_item, column):
        """Вызывается при раскрытии ветви"""
        tree_item.setExpanded(False if tree_item.isExpanded() else True)

        path = self.file_tree.treeItemPath(tree_item)
        self.lineEdit_path.setText(path)
        self.file_tree.newTreeBranch(path, self.getListOfDirectory(path))

    def new_tree_branch(self, tree_item, mass):
        """Создает дочернии элементы для листа дерева"""
        for item in mass:
            QtGui.QTreeWidgetItem(tree_item).setText(0, item)


file_client = FileManager()  
sys.exit(app.exec_())

        