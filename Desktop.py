import os
from PyQt5.QtCore import QObject, QTimer, pyqtSlot, pyqtProperty
from Exceptions import SFTPError, PermissionDeniedError

class Desktop(QObject):
    def __init__(self, engine, client):
        super().__init__()
        self.engine = engine
        self.client = client
        self.engine.rootContext().setContextObject(self)

    def console_write(self, string):
        self.engine.rootObjects()[0].new_console_message.emit(string)

    def start(self):
        self.engine.rootObjects()[0].show()
        self.channel = self.client.invoke_shell(term = 'xfce4-terminal') #xfce4-terminal, xterm-256color, linux

        self.sftp_client = self.client.open_sftp()

        self.show_dir_list('')

        self.timer = QTimer()
        self.timer.start(100)
        def console_update():
            if self.channel.recv_ready():
                nbytes = 12800
                line = self.channel.recv(nbytes)
                #f = open('text.txt', 'bw')
                #print(line)
                #f.write(line)
                self.console_write(line.decode('utf-8'))
        self.timer.timeout.connect(console_update)

    @pyqtSlot(str, str)
    def move(self, from_path, to_path):
        is_local = lambda path: path[:7] == "file://"

        try:
            if is_local(from_path) and not is_local(to_path):
                print('put(' + from_path[7:] + ', ' + to_path + ')')
                #self.sftp_client.put(from_path[7:], to_path + '/' + from_path.split('/')[-1])

            if not is_local(from_path) and is_local(to_path):
                print('get(' + from_path + ', ' + to_path[7:]  + ')')
                #self.sftp_client.get(from_path, to_path[7:] + '/' + from_path.split('/')[-1])

        except Exception as e:
            print(e)

        finally:
            if not is_local(from_path):
                self.show_dir_list('/'.join(from_path.split('/')[:-1]))
            elif not is_local(to_path):
                self.show_dir_list(to_path)

        #self.sftp_client.get(remotepath, localpath)

    @pyqtSlot(str)
    def show_dir_list(self, path):
        try:
            norm_path = self.sftp_client.normalize('/' + path)
            data = [[str(SFTPAttributes.st_mode), 
                     str(SFTPAttributes.st_size),
                     str(SFTPAttributes.filename)] for SFTPAttributes in self.sftp_client.listdir_attr(norm_path)]
        except PermissionError:
            PermissionDeniedError().show()
        except Exception as e:
            print(e)
        else:
            self.engine.rootObjects()[0].remoteHost_showFolder(data, norm_path)

    @pyqtSlot(str) #Отправляет команду через self.channel на сервер
    def send_command(self, command):
        self.channel.send(command + '\n')