import paramiko
from modules.ui_class.ui_Connection import Ui_Dialog_connection
from modules.Exceptions import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QObject
#import ui_Connection

class Settings:
	"""docstring for Settings"""
	def __init__(self, path):
		file = open(path, 'r')
		self.data = {}
		for line in file:
			key, value = line[:-1].split(' = ')[:2]
			self.data[key] = value
		
	def __getitem__(self, key):
		if key in self.data:
			return self.data[key]


class ConnectionManager(QObject):
	"""Создание SSH тунеля и отображение окна настроек соеденения"""
	signalOnConnect = pyqtSignal() #Сигнал отправляется при успешном подключении через SSH
	#signalOnDisconnect = pyqtSignal() #Сигнал отправляется при потере подключения

	def __init__(self):
		super().__init__()

		self.window = QWidget()
		self.ui = Ui_Dialog_connection()
		self.ui.setupUi(self.window)

		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	def load_settings(self, settings):
		self.settings = settings
		self.ui.lineEdit_host.setText(self.settings['host'])
		self.ui.lineEdit_user.setText(self.settings['user'])
		self.ui.lineEdit_secret.setText(self.settings['secret'])
		self.ui.lineEdit_port.setText(self.settings['port'])
		self.ui.lineEdit_terminal_type.setText(self.settings['terminal_type'])

	def connect(self):
		"""Устанавливает подключение. Если подключение установленно посылает сигнал signalOnConnect"""
		try:
			self.client.connect(hostname = self.ui.lineEdit_host.text(), 
								port = int(self.ui.lineEdit_port.text()), 
								username = self.ui.lineEdit_user.text(), 
								password = self.ui.lineEdit_secret.text())

		except paramiko.ssh_exception.BadHostKeyException:
			BadHostKeyError().show()
		except paramiko.ssh_exception.AuthenticationException:
			AuthenticationError().show()
		except paramiko.ssh_exception.SSHException:
			SSHConnectionError().show()

		except OSError as error:
			if error.errno == 8:
				HostError().show()
			elif type(error) == paramiko.ssh_exception.NoValidConnectionsError:
				PortError().show()
			else:
				print('OSError (Errno:', error.errno, ')\n', type(error))
				
		except Exception as error:
			print(type(error),'\n', error)

		else:
			self.signalOnConnect.emit()

	def show(self):
		self.window.show()

	def hide(self):
		self.window.hide()

	def set_buttons_events(self, button_load_func = None, button_connect_func = None, button_exit_func = None):
		if button_load_func:
			self.button_load_func = button_load_func
			self.ui.pushButton_load.clicked.connect(self.button_load_func)

		if button_connect_func:
			self.button_connect_func = button_connect_func
			self.ui.pushButton_connect.clicked.connect(self.button_connect_func)

		if button_exit_func:
			self.button_exit_func = button_exit_func
			self.ui.pushButton_exit.clicked.connect(self.button_exit_func)