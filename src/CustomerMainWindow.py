#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CustomerMainWindow(QWidget):
    def __init__(self):
        super(CustomerMainWindow,self).__init__()

        self.setWindowTitle("Custormer")
        self.restoran_list_lbl = QLabel("Choose restoran:")
        self.restoran_list = QComboBox()
        self.menu_l_lbl = QLabel("Look at menu:")
        self.menu_l = QComboBox()
        self.restoran_location_lbl = QLabel("Restoran location:")
        self.restoran_location_e = QLineEdit()
        self.order_btn = QPushButton("Order!")
        self.restoran_rate_lbl = QLabel("Restoran rate:")
        self.restoran_rate_e = QLineEdit()
        self.rate_btn = QPushButton("Rate!") # shows window for restoran rate
        self.logout_btn = QPushButton("Leave")

        self.layout = QGridLayout()

        self.layout.addWidget(self.restoran_list_lbl)
        self.layout.addWidget(self.restoran_list)
        self.layout.addWidget(self.menu_l_lbl)
        self.layout.addWidget(self.menu_l)
        self.layout.addWidget(self.restoran_location_lbl)
        self.layout.addWidget(self.restoran_location_e)
        self.layout.addWidget(self.order_btn)
        self.layout.addWidget(self.restoran_rate_lbl)
        self.layout.addWidget(self.restoran_rate_e)
        self.layout.addWidget(self.rate_btn)
        self.layout.addWidget(self.logout_btn)

        self.setLayout(self.layout)

        self.connect(self.logout_btn,SIGNAL("clicked()"),self,SLOT("close()"))
        self.connect(self.order_btn,SIGNAL("clicked()"),self,SLOT("order()"))

    @pyqtSlot()
    def order(self):
        print "CustomerWindow::order()::Order called"



