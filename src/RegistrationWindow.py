#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from DB_Manager import DB_Manager

'''
Registration form.
'''

class RegistrationWindow(QWidget):
    def __init__(self,user_type):
        super(RegistrationWindow,self).__init__()

        self.dbm = DB_Manager()
        self.user_type_map = {0:"restorator",1:"seller",2:"customer"}
        self.user_type = user_type

        self.name_lbl = QLabel("Enter name:")
        self.name_e = QLineEdit()
        self.pass_lbl = QLabel("Enter pass:")
        self.pass_e = QLineEdit()
        #self.user_type_lbl = QLabel("Choose user type:")
        #self.user_type_combo = QComboBox()
        
        #self.user_type_combo.addItem("restorator")
        #self.user_type_combo.addItem("seller")
        #self.user_type_combo.addItem("customer")

        self.ok_btn = QPushButton("Register")
        self.close_btn = QPushButton("Close")

        self.layout = QGridLayout()
        self.layout.addWidget(self.name_lbl)
        self.layout.addWidget(self.name_e)
        self.layout.addWidget(self.pass_lbl)
        self.layout.addWidget(self.pass_e)
        self.layout.addWidget(self.ok_btn)
        self.layout.addWidget(self.close_btn)
        #self.layout.addWidget(self.user_type_lbl)
        #self.layout.addWidget(self.user_type_combo)

        self.setLayout(self.layout)

        self.connect(self.close_btn,SIGNAL("clicked()"),self,SLOT("close()"))
        self.connect(self.ok_btn,SIGNAL("clicked()"), self,SLOT("register()"))


    @pyqtSlot()
    def register(self):
        print "RegistrationWindow::register::user_type",self.user_type
        user_name = str(self.name_e.text())
        user_pass = str(self.pass_e.text())
        print "user_name",user_name,"user_pass",user_pass
        
        if self.dbm.check_unique(self.user_type_map[self.user_type],user_name):
            if self.user_type == 0:
                self.dbm.add_restorator(user_name,user_pass)
            elif self.user_type == 1:
                self.dbm.add_seller(user_name,user_pass)
            else:
                self.dbm.add_customer(user_name,user_pass)
            self.show_info("Registration successfull.")
            self.close()
        else:
            self.show_info("Registration failed. Enter another user name.")

    def show_info(self,e):
        msgBox = QMessageBox()
        msgBox.setText(str(e))
        msgBox.setStandardButtons(QMessageBox.Ok)
        ret = msgBox.exec_()
        #sys.exit()
