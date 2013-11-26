#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from DB_Manager import DB_Manager
from CustomerMainWindow import CustomerMainWindow
from SellerMainWindow import SellerMainWindow

class AuthorizationWindow(QWidget):
    def __init__(self, user_type):
        super(AuthorizationWindow,self).__init__()

        self.setWindowTitle("Authoriazation")

        self.dbm = DB_Manager()
        self.user_type_map = {0:"restorator",1:"seller",2:"customer"}
        self.user_type = user_type
        
        self.ok_btn = QPushButton("Ok")
        self.cancel_btn = QPushButton("Cancel")
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
        self.layout.addWidget(self.cancel_btn)

        self.setLayout(self.layout)

        self.customer_mw = CustomerMainWindow()
        self.seller_mw = SellerMainWindow()

        self.connect(self.ok_btn,SIGNAL("clicked()"), self, SLOT("validate()"))
        self.connect(self.cancel_btn,SIGNAL("clicked()"),self,SLOT("close()"))

    @pyqtSlot()
    def test(self):
        print "AuthorizationWindow::test"

    @pyqtSlot()
    def validate(self):
        '''
        Validate authorization data.
        '''
        print str(self.login_edit.text()), str(self.pass_edit.text())
        print self.user_type_map[self.user_type] 
        if self.dbm.find_user_for_authorization(self.user_type_map[self.user_type],str(self.login_edit.text()), str(self.pass_edit.text()) ):
            print "Authorization successfull."
            self.show_info("Authorization successfull. Welcome!")
            
            if self.user_type == 2:
                print "Starting customer main window"
                self.customer_mw.show()
            elif self.user_type == 1:
                print "Starting seller main window"
                self.seller_mw = SellerMainWindow( str(self.login_edit.text()) )
                self.seller_mw.show()
            
            self.close()
        else:
            print "Authorization failed."
            self.show_info("Authoriztion failed. Please, check your login or password.")
            self.close()

    def show_info(self,e):
        msgBox = QMessageBox()
        msgBox.setText(str(e))
        msgBox.setStandardButtons(QMessageBox.Ok)
        ret = msgBox.exec_();
