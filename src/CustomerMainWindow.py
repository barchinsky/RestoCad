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
        self.free_place_count_lbl = QLabel("Free places:")
        self.free_place_count_e = QLineEdit()
        self.order_btn = QPushButton("Order place!")
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
        self.layout.addWidget(self.free_place_count_lbl)
        self.layout.addWidget(self.free_place_count_e)
        self.layout.addWidget(self.order_btn)
        self.layout.addWidget(self.restoran_rate_lbl)
        self.layout.addWidget(self.restoran_rate_e)
        self.layout.addWidget(self.rate_btn)
        self.layout.addWidget(self.logout_btn)

        self.setLayout(self.layout)

        self.connect(self.logout_btn,SIGNAL("clicked()"),self,SLOT("close()")) # logout when logout button clicked
        self.connect(self.order_btn,SIGNAL("clicked()"),self,SLOT("order()")) # call order() when button order clicked
        self.connect(self.restoran_list,SIGNAL("currentIndexChanged(int)"),self, SLOT("update()") ) # update form according to the new restoran
        self.connect(self.rate_btn,SIGNAL("clicked()"),self,SLOT("rate()"))
 
    @pyqtSlot()
    def order(self):
        restoran = str(self.restoran_list.currentText())
        print "CustomerWindow::order()::Order called"

        self.dbm.update_free_places(restoran)
        self.update()
        #if self.

    @pyqtSlot()
    def update(self): # update form data
        restoran = str(self.restoran_list.currentText())
        self.load_restoran_menu(restoran) # loads restoran menu
        self.set_rate(restoran) # show choosen restoran rate
        self.set_location(restoran)
        self.load_free_places(restoran)

    def load(self): # loads form data
        self.load_restoran_list()
        restoran = str(self.restoran_list.currentText())
        self.load_restoran_menu(restoran) # loads restoran menu
        self.set_rate(restoran) # show choosen restoran rate
        self.set_location(restoran)
        self.load_free_places(restoran)

    def load_restoran_list(self): # loads restoran list from db
        self.restoran_list.clear()
        restoran_list = self.dbm.get_restoran_list()

        for restoran in restoran_list:
            self.restoran_list.addItem(restoran)

    def load_free_places(self,restoran):
        self.free_place_count_e.clear()
        self.free_place_count_e.setText( self.dbm.get_free_places_number(restoran) )

    @pyqtSlot()
    def load_restoran_menu(self,restoran): # load restoran menu
        print "Load menu called."
        self.clean_menu_combo()
        #restoran = str(self.restoran_list.currentText())
        menu = self.dbm.get_restoran_menu(restoran)
        print "current text: %s"%(restoran)

        for dish in menu:
            self.menu_l_c.addItem(dish)

        #self.set_location(restoran)

    @pyqtSlot()
    def rate(self):
        print "rate::rate()"
        restoran = str(self.restoran_list.currentText())
        print "rate::Restoran:%s"%restoran
        grade = str(self.restoran_rate_e.text())
        self.dbm.set_restoran_grade(restoran,grade)

    def clean_menu_combo(self):
        print "Clean combo"
        print (self.menu_l_c.count())
        self.menu_l_c.clear()
        print "After removing:" + str(self.menu_l_c.count())

    def set_location(self,restoran):
        location = self.dbm.get_restoran_location(restoran)
        self.restoran_location_e.setText(location)

    def set_rate(self,restoran):
        self.restoran_rate_e.setText( str( self.dbm.get_restoran_grade(restoran) ) )
