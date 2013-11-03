#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from DB_Manager import DB_Manager

class AuthorizationWindow(QWidget):
    def __init__(self, user_type):
        super(AuthorizationWindow,self).__init__()

        self.dbm = DB_Manager()
        self.user_type_map = {0:"restorator",1:"seller",2:"customer"}
        self.user_type = user_type
        
        self.ok_btn = QPushButton("Ok")
        self.login_lable = QLabel("Login:")
        self.login_edit = QLineEdit()
        self.pass_lable = QLabel("Password:")
        self.pass_edit = QLineEdit()

        self.layout = QGridLayout()

        self.layout.addWidget(self.login_lable,0,0)
        self.layout.addWidget(self.login_edit,0,1)
        self.layout.addWidget(self.pass_lable)
        self.layout.addWidget(self.pass_edit)
        self.layout.addWidget(self.ok_btn)

        self.setLayout(self.layout)

        self.connect(self.ok_btn,SIGNAL("clicked()"),self,SLOT("test()"))
        self.connect(self.ok_btn,SIGNAL("clicked()"), self, SLOT("validate()"))

    @pyqtSlot()
    def test(self):
        print "AuthorizationWindow::Ok!"

    @pyqtSlot()
    def validate(self):
        '''
        Validate authorization data.
        '''
        print str(self.login_edit.text()), str(self.pass_edit.text())
        if self.dbm.find_user_for_authorization('seller',str(self.login_edit.text()), str(self.pass_edit.text()) ):
            print "Authorization successfull."
            self.show_info("Authorization successfull. Welcome!")
            self.close()

    def validate_seller(self):
        pass
    
    def validate_customer(self):
        pass

    def validate_restorator(self):
        pass

    def show_info(self,e):
        msgBox = QMessageBox()
        msgBox.setText(str(e))
        msgBox.setStandardButtons(QMessageBox.Ok)
        ret = msgBox.exec_();



          
