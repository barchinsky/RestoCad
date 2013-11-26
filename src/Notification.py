from PyQt4.QtCore import *
from PyQt4.QtGui import *

def show_info(e):
    msgBox = QMessageBox()
    msgBox.setText(str(e))
    msgBox.setStandardButtons(QMessageBox.Ok)
    ret = msgBox.exec_();
