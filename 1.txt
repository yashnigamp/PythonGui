import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from tkinter.test.support import widget_eq
from PyQt5.QtCore import Qt

class ya(QDialog):
    def __init__(self):
        super(ya,self).__init__()
        loadUi('ya.ui',self)
        self.setWindowTitle('ya PyQt5 Gui')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label1.SetText('Welcome:'+self.lineEdit1.text())
    
app = QApplication(sys.argv)
widget = ya()
widget.show()
sys.exit(app.exec_())   