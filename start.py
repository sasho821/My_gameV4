import imp
import sys
from PyQt5.QtWidgets import QApplication

from UI.ui_window import startForm

app = QApplication([])

reg_win = startForm()
reg_win.show()

app.exec_()
