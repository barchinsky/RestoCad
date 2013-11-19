#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from DB_Manager import DB_Manager

class CustomerMainWindow(QWidget):
    def __init__(self):
        super(CustomerMainWindow,self).__init__()
        self.dbm = DB_Manager()

        self.setWindowTitle("Custormer")
        self.restoran_list_lbl = QLabel("Choose restoran:")
        self.restoran_list = QComboBox()
        self.menu_l_lbl = QLabel("Look at menu:")
        self.menu_l_c = QComboBox()
        self.restoran_location_lbl = QLabel("Restoran location:")
        self.restoran_location_e = QLineEdit()
        self.order_btn = QPushButton("Order!")
        self.restoran_rate_lbl = QLabel("Restoran rate:")
        self.restoran_rate_e = QLineEdit()
        self.rate_btn = QPushButton("Rate!") # shows window for restoran rate
        self.logout_btn = QPushButton("Exit")

        self.load()

        self.layout = QGridLayout()

        self.layout.addWidget(self.restoran_list_lbl)
        self.layout.addWidget(self.restoran_list)
        self.layout.addWidget(self.menu_l_lbl)
        self.layout.addWidget(self.menu_l_c)
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
        self.connect(self.restoran_list,SIGNAL("currentIndexChanged(int)"),self, SLOT("load_restoran_menu()") )

    @pyqtSlot()
    def order(self):
        print "CustomerWindow::order()::Order called"

    def load(self):
        self.load_restoran_list()
        #self.load_restoran_menu()

    def load_restoran_list(self):
        restoran_list = self.dbm.get_restoran_list()

        for restoran in restoran_list:
            self.restoran_list.addItem(restoran)

    @pyqtSlot()
    def load_restoran_menu(self):
        print "Load menu called."
        self.clean_menu_combo()
        restoran = str(self.restoran_list.currentText())
        menu = self.dbm.get_restoran_menu(restoran)
        print "current text: %s"%(restoran)

        for dish in menu:
            self.menu_l_c.addItem(dish)

        self.set_location(restoran)



    def clean_menu_combo(self):
        print "Clean combo"
        print (self.menu_l_c.count())
        self.menu_l_c.clear()
        print "After removing:" + str(self.menu_l_c.count())

    def set_location(self,restoran):
        location = self.dbm.get_restoran_location(restoran)
        print restoran
        print location
        self.restoran_location_e.setText(location)

        



