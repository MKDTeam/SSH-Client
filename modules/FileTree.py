from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QTreeWidget, QTreeWidgetItem
from  modules.ui_class.ui_FileTree import Ui_file_manager

class FileTreeWidget(QTreeWidget):
    """Виджет дерева файлов основаный на QTreeWidget"""
    def __init__(self, arg = None):
        super().__init__(arg)
        self.arg = arg
        self.separator = '/'    
        self.root_items = [] #список содержащий корневые каталоги
        self.column_path = 0 #колонка таблицы в которой указан путь
        self.column_type = 1 #колонка таблицы в которой указан тип файла
        
        self.setColumnCount(2)
        self.setHeaderLabels(['Имя файла', 'Тип файла'])
        self.header().setResizeMode(1)
        self.setSortingEnabled(True)
        self.setExpandsOnDoubleClick(False)

    def setSeparator(self, char):
        """Установка - self.separator - разделителя в пути к файлу"""
        self.separator = char

    def treeItemPath(self, item):
        current_item = item
        path = ""
        while current_item:
            path = current_item.text(self.column_path) + path
            current_item = current_item.parent()
        return path     

    def newTreeBranch(self, path, dir_array):
        """Создает по указанному пути дирректории указанные в dir_array, путь формате /bin/example/"""
        for directory in dir_array:
            self.newTreeItem(str(path + directory))

    def newTreeItem(self, path):
        """Создает элемент дерева и всю необходимую структуру используя указаный путь"""
        dir_type = path[-1]
        path = path[0:-1]
        
        directories = path.split(self.separator)
        directories = [directory + self.separator for directory in directories]

        current_item = None
        for root in self.root_items:
            if root.text(self.column_path) == directories[0]:
                current_item = root
                break

        if current_item == None: #корневого элемента не существует
            current_item = QTreeWidgetItem(self)
            self.root_items.append(current_item)
            #print([s.text(0) for s in self.root_items])
            for directory in directories:
                if directory != directories[-1]:
                    current_item.setText(self.column_path, directory)
                    current_item = QTreeWidgetItem(current_item)
                else:
                    current_item.setText(self.column_path, directory[0:-1])
        else:
            for  directory in directories:
                if directory == directory[0]: continue #пропускаем корневую директорию
                children = [] #список детей для текущего элемента current_item
                index = 0    
                while index < current_item.childCount():
                    children.append(current_item.child(index))
                    index += 1

                for child in children:
                    if child.text(self.column_path) == directory:
                        current_item = child
                        break

                if current_item.text(self.column_path) != directory: 
                    current_item = QTreeWidgetItem(current_item)
                    current_item.setText(self.column_path, directory)
                if current_item.text(self.column_path) == directories[-1]:
                    current_item.setText(self.column_path, directories[-1][0:-1])

        if dir_type == '/':
            current_item.setText(self.column_type,  'Каталог')
            current_item.setText(self.column_path,  current_item.text(self.column_path) + dir_type)
        elif dir_type == '|':
            current_item.setText(self.column_type,  'FIFO')
        elif dir_type == '@':
            current_item.setText(self.column_type,  'Символическая ссылка')
        elif dir_type == '=':
            current_item.setText(self.column_type,  'Сокет')
        else:
            current_item.setText(self.column_type,  '')
            current_item.setText(self.column_path,  current_item.text(self.column_path) + dir_type)
        
    def isElementExists(self, path):
        """Проверяет существование элемента, False - элемента не существует"""
        directories = path.split(self.separator)
        directories = [directory + self.separator for directory in directories]

        directories.reverse()
        candidates = self.findItems(directories[0], QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)
        
        if len(candidates) == 0:
            return False
            
        for candidate in candidates: #проверка каждого из кандидатов
            current_item = candidate
            for directory in directories: #пробегаем весть путь от конечной дериктории до начальной
                if current_item.text(0) != directory:
                    break
                if directory == directories[-1]:
                    return True
                current_item = current_item.parent()
                
        return False

class FileManager(Ui_file_manager):
    """Графический менеджер работы с файлами"""
    def __init__(self):
        self.window = QWidget()
        self.setupUi(self.window)

        self.file_tree = FileTreeWidget()
        self.file_tree.setSeparator('/')

        self.treeWidget.addWidget(self.file_tree)

        self.file_tree.itemClicked.connect(self.treeItemActivated)

        #QtCore.QObject.connect(self.file_tree , QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self.treeItemActivated)
        
    def start(self, client):
        self.client = client
        self.window.show()
        if not self.file_tree.topLevelItem(0):
            self.file_tree.newTreeBranch('/', self.getListOfDirectory('/'))
            self.file_tree.topLevelItem(0).setExpanded(True)


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
