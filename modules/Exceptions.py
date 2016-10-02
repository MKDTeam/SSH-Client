class Error(Exception):
	"""Базовый класс для исключений в этом модуле."""
	pass
 
class ModulesError(Error):
	"""Exception raised for errors in the input.
	Исключение возбуждается для ошибок в вводе.
 
	Attributes:
		expression -- input expression in which the error occurred
				   -- входное выражение, в котором произошла ошибка
		message -- explanation of the error
				-- объяснение ошибки
	"""
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message
 
class TransitionError(Error):
	"""Raised when an operation attempts a state transition that's not allowed.
	Возникает при попытке операции перехода, которая не допускается.
 
	Attributes:
		previous -- state at beginning of transition
				 -- состояние в начале перехода
		next -- attempted new state
			 -- нового состояния, к которому пытаются перейти
		message -- explanation of why the specific transition is not allowed
				-- объяснение, почему конкретный переход не допускается
	"""
	def __init__(self, previous, next, message):
		self.previous = previous
		self.next = next
		self.message = message