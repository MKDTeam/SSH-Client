from PyQt5.QtGui import QFont, QTextCursor, QFontMetrics, QKeyEvent
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtCore import Qt, QEvent, QTimer

settings = {'time_console_update':100,  # ms            - временной промежуток через который проверяется поступление данных с сервера
            'connection_speed': 128     # kilobyte/s    - скорость поступления данных (исходя из них выбирается размер буфера)
            }

class Console(QPlainTextEdit):
    """Виджет консоли основаный на QPlainTextEdit"""
    input_buffer = ''

    def __init__(self, arg = None):
        #Ограничение подвижности текстового курсора
        super().__init__(arg)
        self.setWindowTitle('Console')
        self.font = QFont()
        self.font.setFamily("Courier New")
        self.setFont(self.font)
        self.curent_cursor_position = 0
        self.input_cursor = QTextCursor(self.document()) #используется для отображения результатов команд
        self.command_cursor = QTextCursor(self.document()) #используется для ввода команд
        def positionChecker():
            if self.textCursor().position() < self.curent_cursor_position:
                self.setTextCursor(self.input_cursor)
        self.cursorPositionChanged.connect(positionChecker)
        self.resize(80, 24)

    def resize(self, x, y):
        char_width = QFontMetrics(self.font).width('aaaaaaaabbcccddddeeeeeeeeeeeeffgghhhhhhiiiiiiijkllllmmnnnnnnoooooooopprrrrrrsssssstttttttttuuuvwwxyy') / 100
        char_height = QFontMetrics(self.font).height()
        super().resize(x * char_width, y * char_height)

    def clearConsole(self):
        for x in range(len(self.input_buffer)):
            super().keyPressEvent(QKeyEvent(QEvent.KeyPress, Qt.Key_Backspace,  Qt.KeyboardModifiers()))

    def start(self, client):
        self.channel = client.invoke_shell(term = 'xfce4-terminal')

        #Проверка поступления данных с сервера 
        self.timer = QTimer()
        self.timer.start(settings['time_console_update'])
        def console_update():
            if self.channel.recv_ready():
                nbytes = settings['connection_speed'] * settings['time_console_update']
                line = self.channel.recv(nbytes)
                self.input_cursor.insertText(line.decode('utf-8'))
                self.curent_cursor_position = self.input_cursor.position()
        self.timer.timeout.connect(console_update)

        super().show()

    def exec_command(self, command):
        if len(command) == 1 and ord(command) < 32: # если поступил управляющий символ
            self.channel.send(command)
        else: # обычная команда
            self.channel.send(command + '\n')

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Enter or keyEvent.key() == Qt.Key_Return: #отправка команды
            self.exec_command(self.input_buffer)
            self.clearConsole()
            self.input_buffer = ''
            return
        elif keyEvent.key() == Qt.Key_Backspace: #стереть символы
            if len(self.input_buffer) == 0:
                return
            self.input_buffer = self.input_buffer[:-1]
            super().keyPressEvent(keyEvent)
            return
        elif keyEvent.key() == Qt.Key_Escape: #прервать выполнение команды
            #self.exec_command(chr(27) + 'C')
            self.exec_command(chr(3))
            self.clearConsole()
            self.input_buffer = ''
            return
        super().keyPressEvent(keyEvent)
        self.input_buffer += self.document().toPlainText()[-1]

    def mousePressEvent(self, mouseEvent):
        #self.setFocus()
        super().mousePressEvent(mouseEvent)

    def mouseDoubleClickEvent(self, mouseEvent):
        super().mouseDoubleClickEvent(mouseEvent)

    def contextMenuEvent(self, contextMenuEvent):
        super().contextMenuEvent(contextMenuEvent)

