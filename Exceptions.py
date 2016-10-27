from PyQt5.QtWidgets import QMessageBox

class Error(Exception):
	"""Базовый класс для исключений в этом модуле."""
	def __init__(self, message):
		self.message = message
		self.widget = QMessageBox()
		self.widget.setText(message)

	def __str__(self):
		return self.message
		
	def show(self):
		self.widget.exec_()
 
#--------------------------------------------------------------------

class SSHConnectionError(Error):
	"""Исключение возникающее при работе с SSH соединением (кроме работы с файлами)."""
	def __init__(self, additional_message):
		super().__init__("Ошибка установки SSH подключения")
		self.widget.setInformativeText(additional_message)

class HostError(SSHConnectionError):
	"""Ошибка подключения к хосту"""
	def __init__(self):
		super().__init__("Не удается открыть соединение к указанному хосту.")

class PortError(SSHConnectionError):
	"""Ошибка подключения к порту"""
	def __init__(self):
		super().__init__("Соединение с хостом было установленно, но попытка подключится провалилась. Не получен ответ от SSH сервера по указанному порту.")
		
class AuthenticationError(SSHConnectionError):
	"""Ошибка аутентификации"""
	def __init__(self):
		super().__init__("Некорректное имя пользователя или пароль.")

class BadHostKeyError(SSHConnectionError):
	"""Ошибка соединения с сервером - ошибочные ключи"""
	def __init__(self):
		super().__init__("Ключи сервера не являются подлинными.")

#--------------------------------------------------------------------		
 
class SFTPError(Error):
	"""Исключение возникающее при работе с SFTP."""
	def __init__(self, additional_message):
		super().__init__("Операция над файлом не может быть выполнена.")
		self.widget.setInformativeText(additional_message)

class PermissionDeniedError(SFTPError):
	"""Ошибка подключения к хосту"""
	def __init__(self):
		super().__init__("Доступ к файлу запрещен.")