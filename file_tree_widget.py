import sys
from PyQt4 import QtCore, QtGui

class FileTreeWidget(QtGui.QTreeWidget):
    """Виджет дерева файлов основаный на QTreeWidget"""
    def __init__(self, arg = None):
        super().__init__(arg)
        self.arg = arg
        self.separator = '/'    
        self.root_items = [] #список содержащий корневые каталоги
        self.column_path = 0 #колонка таблицы в которой указан путь
        self.column_type = 1 #колонка таблицы в которой указан путь

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
            current_item = QtGui.QTreeWidgetItem(self)
            self.root_items.append(current_item)
            #print([s.text(0) for s in self.root_items])
            for directory in directories:
                if directory != directories[-1]:
                    current_item.setText(self.column_path, directory)
                    current_item = QtGui.QTreeWidgetItem(current_item)
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
                    current_item = QtGui.QTreeWidgetItem(current_item)
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

#app = QtGui.QApplication(sys.argv)
#
#base_widget = QtGui.QWidget()
#base_widget.resize(500, 800)
#base_widget.setWindowTitle("Тестовое окно")
#
##
#tree = FileTreeWidget(base_widget)
#print("///////////////////////////////////////////////////////")
#tree.newTreeItem("/bin/test/project/example/1/run.exe")
#tree.newTreeItem("/var/test/project/example/1/run.exe")
#tree.newTreeBranch("/var/", list("example"))
#print(tree.isElementExists("/var/test/project/example/1/"))
#print("///////////////////////////////////////////////////////")
##
#
#grid_layout = QtGui.QGridLayout(base_widget)
#grid_layout.addWidget(tree)
#
#base_widget.show()
#
#sys.exit(app.exec_())