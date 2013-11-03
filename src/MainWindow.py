#!/usr/bin/python
# simple.py

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
from StartUpWindow import StartUpWindow

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__(parent)
        self._start_up_widget = StartUpWindow(self)

        self.setWindowTitle('RestoCad')

        self.setCentralWidget(self._start_up_widget)

        self.connect(self._start_up_widget.cancel_btn,SIGNAL("clicked()"),self,SLOT("close()")) # close window if startup window closed

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()

    sys.exit(app.exec_())
