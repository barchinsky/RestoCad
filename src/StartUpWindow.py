#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from AuthorizationWindow import AuthorizationWindow
from RegistrationWindow import RegistrationWindow

class StartUpWindow(QWidget):
    def __init__(self,parent):
        super(StartUpWindow,self).__init__(parent)

        self.layout = QGridLayout()

        self.ok_btn = QPushButton("Ok")
        self.cancel_btn = QPushButton("Cancel")

        self.action_type_combo = QComboBox()
        self.action_label = QLabel("Action:")
        self.action_type_combo.addItem("Authorization")
        self.action_type_combo.addItem("Registration")

        self.user_type_combo = QComboBox()
        self.user_type_label = QLabel("User:")
        self.user_type_combo.addItem("Restorator")
        self.user_type_combo.addItem("Seller")
        self.user_type_combo.addItem("Customer")

        self.layout.addWidget(self.action_label,0,0)
        self.layout.addWidget(self.action_type_combo,0,1)
        self.layout.addWidget(self.user_type_label)
        self.layout.addWidget(self.user_type_combo)
        self.layout.addWidget(self.ok_btn)
        self.layout.addWidget(self.cancel_btn)

        self.setLayout(self.layout)

        self.connect(self.cancel_btn,SIGNAL("clicked()"),self,SLOT("close()"))
        self.connect(self.ok_btn,SIGNAL("clicked()"),self, SLOT("confirm_action()"))

    @pyqtSlot()
    def confirm_action(self):
        '''
        User indexes:
            0-Restorator
            1-Seller
            2-Customer

        Action indexes:
            1-Registration
            0-Authorization
        '''
        user_type = self.user_type_combo.currentIndex()
        action_type = self.action_type_combo.currentIndex()
        print "User type:%s.\nAction type:%s."%(user_type,action_type)

        if action_type == 1:
            print "Registration called."
            self.reg_window = RegistrationWindow(user_type)
            self.connect(self.reg_window.ok_btn, SIGNAL("clicked()"),SLOT("enable()"))
            self.connect(self.reg_window.close_btn, SIGNAL("clicked()"),SLOT("enable()"))
            self.setDisabled(1)
            self.reg_window.show()
        elif action_type == 0:
            print "Authorization called."
            self.auth_window = AuthorizationWindow(user_type)
            self.connect(self.auth_window.ok_btn, SIGNAL("clicked()"),SLOT("enable()"))

            self.setDisabled(1)
            self.auth_window.show()

    def show_info(self,e):
        msgBox = QMessageBox()
        msgBox.setText(str(e))
        msgBox.setStandardButtons(QMessageBox.Ok)
        ret = msgBox.exec_();
        sys.exit()

    @pyqtSlot()
    def enable(self):
        self.setDisabled(0)
