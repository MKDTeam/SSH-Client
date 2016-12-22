import os
import shutil
import time
from PyQt5.QtCore import QObject, QTimer, pyqtSlot, pyqtProperty
from Exceptions import SFTPError, PermissionDeniedError
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QWidget

class Desktop(QObject):
    def __init__(self, engine, client, settings):
        super().__init__()
        self.engine = engine
        self.client = client
        self.settings = settings
        self.engine.rootContext().setContextObject(self)

    def console_write(self, string):
        self.engine.rootObjects()[0].new_console_message.emit(string)

    def start(self):
        self.engine.rootObjects()[0].show()
        self.channel = self.client.get_transport().open_session() #xfce4-terminal, xterm-256color, linux
        self.channel.get_pty(self.settings['terminal_type'])
        self.channel.invoke_shell()
        #self.channel.set_environment_variable()

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

    @pyqtSlot(str)
    def rename(self, path):
        is_local = lambda p: p[:7] == "file://"

        if not is_local(path):
            #msgBox = QInputDialog()
            #windows = 
            new_filename, ok = QInputDialog.getText(QWidget(), 'Изменение имени файла', 'Введите новое имя:')
            #new_filename, ok = QInputDialog.getText(QWidget(), 'Change the file name', 'Enter a new file name:')
            if ok:
                new_path = path.split('/')[:-1]
                new_path.append(new_filename)
                new_path = '/'.join(new_path)
                self.sftp_client.rename(path, new_path)
                #stdin, stdout, stderr = self.client.exec_command('mv "{0}" "{1}"'.format(path, new_path))
                time.sleep(1)
                self.show_dir_list('/'.join(path.split('/')[:-1]))

    @pyqtSlot(str, bool)
    def copy(self, path, isDir):
        is_local = lambda p: p[:7] == "file://"

        if not is_local(path):
            #msgBox = QInputDialog()
            #windows = 
            msgBox = QMessageBox()
            msgBox.setText("Копирование файла")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setInformativeText('Вы уверены что хотите создать копию файла?')
            answer = msgBox.exec_()


            if answer == QMessageBox.Yes:
                if isDir:
                    new_path = path + '-copy'
                    self.client.exec_command('cp -r "{0}" "{1}"'.format(path, new_path))
                else:
                    new_path = path.split('.')
                    new_path = '.'.join(new_path[:-1]) + '-copy.' + new_path[-1]
                    self.client.exec_command('cp "{0}" "{1}"'.format(path, new_path))

                time.sleep(1)
                self.show_dir_list('/'.join(path.split('/')[:-1]))


    @pyqtSlot(str)
    def MD5_compare(self, dir_path):
        is_local = lambda path: path[:7] == "file://"

        try:
            if not is_local(dir_path):
                msgBox = QMessageBox()
                msgBox.setText("MD5 Script")
                msgBox.setStandardButtons(QMessageBox.Close);
                msgBox.setInformativeText('Ошибка чтения')

                stdin, stdout, stderr = self.client.exec_command('cd ' + dir_path + ' && ' + str(self.settings['MD5_script']))

                MD5_raw_array = stdout.read().decode('utf-8')
                MD5_array = {line.split(' = ')[0]: line.split(' = ')[1] for line in MD5_raw_array.splitlines()}
                MD5_compare_array = {}

                text = ''
                for key, value in MD5_array.items():
                    if value not in MD5_compare_array.keys():
                        MD5_compare_array[value] = []
                    if value in MD5_compare_array.keys():
                        MD5_compare_array[value].append(key)

                for key in MD5_compare_array.keys():
                    if len(MD5_compare_array[key]) > 1:
                        text += 'MD5:' + key + '\n'
                        count = 1
                        for filename in MD5_compare_array[key]:
                            text += '   file #' + str(count) + ': ' + filename[2:] + '\n'
                            count += 1

                msgBox.setInformativeText(text if text != '' else 'Файлы с одинаковым MD5 не найдены')
                msgBox.exec_()

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Ошибка расчета MD5")
            msgBox.setInformativeText(e.__str__())
            msgBox.exec_()

    @pyqtSlot(str, str)
    def move(self, from_path, to_path):
        is_local = lambda path: path[:7] == "file://"

        try:
            if is_local(from_path) and not is_local(to_path):
                self.sftp_client.put(from_path[7:], to_path + '/' + from_path.split('/')[-1])

            if not is_local(from_path) and is_local(to_path):
                self.sftp_client.get(from_path, to_path[7:] + '/' + from_path.split('/')[-1])

            if not is_local(from_path) and not is_local(to_path):
                self.client.exec_command('mv "{0}" "{1}"'.format(from_path, to_path))

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Ошибка перемещения файла")
            msgBox.setInformativeText(e.__str__())
            msgBox.exec_()

        finally:
            time.sleep(1)
            if not is_local(from_path):
                self.show_dir_list('/'.join(from_path.split('/')[:-1]))
            elif not is_local(to_path):
                self.show_dir_list(to_path)

    @pyqtSlot(str, bool)
    def remove(self, path, isDir):
        is_local = lambda p: p[:7] == "file://"
        try:
            msgBox = QMessageBox()
            msgBox.setText("Удаление файла")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setInformativeText('Вы уверены что хотите удалить файл?')
            answer = msgBox.exec_()

            if answer == QMessageBox.Yes:
                if isDir:
                    if is_local(path):
                        shutil.rmtree(path[7:])

                    if not is_local(path):
                        self.client.exec_command('rm -r "{}"'.format(path))

                if not isDir:
                    if is_local(path):
                        os.remove(path[7:])

                    if not is_local(path):
                        self.sftp_client.remove(path)

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Ошибка удаления файла")
            msgBox.setInformativeText(e.__str__())
            msgBox.exec_()

        finally:
            time.sleep(1)
            self.show_dir_list('/'.join(path.split('/')[:-1]))

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
        try:
            if command == chr(3):
                self.channel.send(command)
            else:
                self.channel.send(command + '\n')

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setText("Ошибка отправки команды на сервер")
            msgBox.setInformativeText(e.__str__())
            msgBox.exec_()
