import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_LoadSettings import Ui_Dialog

application = QApplication(sys.argv)

windows = QWidget()
ui = Ui_Dialog()
ui.setupUi(windows)
ui.groupBox.hide()
windows.show()

sys.exit(application.exec_())