import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from tkinter.test.support import widget_eq
app = QApplication(sys.argv)
widget = ya()
widget.show()
sys.exit(app.exec_())   