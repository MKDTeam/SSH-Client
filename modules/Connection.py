import paramiko
from modules.ui_class.ui_Connection import Ui_Dialog_connection
from PyQt4.QtGui import QWidget
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
		return self.data[key]


class ConnectionManager:
	"""Создание SSH тунеля и отображение окна настроек соеденения"""
	def __init__(self):
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
		self.client.connect(self.ui.lineEdit_host.text(), int(self.ui.lineEdit_port.text()), self.ui.lineEdit_user.text(), self.ui.lineEdit_secret.text())
		#return(self.client)

	def show_ui(self):
		self.window.show()

	def hide_ui(self):
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