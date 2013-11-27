#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from DB_Manager import DB_Manager
from Notification import *

class AddProductWidget(QWidget):
    def __init__(self,_parent):
        super(AddProductWidget,self).__init__()
        self.parent = _parent
        self.product_name_lbl = QLabel("Enter product name:")
        self.product_name_e = QLineEdit()
        self.product_price_lbl = QLabel("Enter product  pack price")
        self.product_price_e = QLineEdit()
        self.product_number_lbl = QLabel("Enter product pack number")
        self.product_number_e = QLineEdit()
        self.add_btn = QPushButton("Add")
        self.close_btn = QPushButton("Close")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.product_name_lbl)
        self.layout.addWidget(self.product_name_e)
        self.layout.addWidget(self.product_price_lbl)
        self.layout.addWidget(self.product_price_e)
        self.layout.addWidget(self.product_number_lbl)
        self.layout.addWidget(self.product_number_e)
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.close_btn)

        self.setLayout(self.layout)

        self.connect(self.close_btn,SIGNAL("clicked()"),self,SLOT("close()"))
        self.connect(self.add_btn,SIGNAL("clicked()"),self,SLOT("add()"))

    @pyqtSlot()
    def add(self):
        self.parent.add_product(str(self.product_name_e.text()), str(self.product_price_e.text()), str(self.product_number_e.text()))
        self.close()

class ClientViewWidget(QWidget):
    def __init__(self):
        super(ClientViewWidget,self).__init__()

        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(3)

        self.layout = QGridLayout()

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        

class SellerMainWindow(QWidget):
    def __init__(self,_seller_login=""):
        super(SellerMainWindow,self).__init__()
        print "Seller main window started. User:%s"%_seller_login
        self.dbm = DB_Manager()
        self.product_sold_lbl = QLabel("Product sold:")
        self.product_sold_e = QLineEdit()
        self.add_product_btn = QPushButton("Add product")
        self.close_btn = QPushButton("Close")
        self.manage_products_btn = QPushButton("Manage products")
        self.seller_login = _seller_login
        self.goto_client_list_btn = QPushButton("View clients")

        self.layout = QGridLayout()

        self.layout.addWidget(self.product_sold_lbl)
        self.layout.addWidget(self.product_sold_e)
        self.layout.addWidget(self.add_product_btn)
        self.layout.addWidget(self.manage_products_btn)
        self.layout.addWidget(self.add_product_btn)
        self.layout.addWidget(self.goto_client_list_btn)
        self.layout.addWidget(self.close_btn)

        self.setLayout(self.layout)

        self.connect(self.add_product_btn,SIGNAL("clicked()"),self,SLOT("call_add_product_widget()"))
        self.connect(self.manage_products_btn,SIGNAL("clicked()"), self, SLOT("call_manage_product_widget()"))
        self.connect(self.close_btn,SIGNAL("clicked()"),self,SLOT("close()"))
        self.connect(self.goto_client_list_btn,SIGNAL("clicked()"),self,SLOT("call_clients_widget()"))

        self.load()

    @pyqtSlot()
    def call_add_product_widget(self):
        print "SellerMainWindow::call_add_product_widget()"
        self.add_product_widget = AddProductWidget(self)
        self.add_product_widget.show()
        pass
    @pyqtSlot()
    def call_clients_widget(self):
        print "SellerMainWindow::call_clients_widget()"
        self.cl_table = ClientViewWidget()
        self.cl_table.show()
        pass

    def load(self):
        if self.check_products():
            self.set_product_combo()

    @pyqtSlot()
    def call_manage_product_widget(self):
        print "SellerMainWindow::call_manage_product_widget()"
        pass

    def set_product_combo(self):
        product_list = self.dbm.get_seller_product_list(self.seller_login)
        for item in product_list:
            self.product_combo.addItem(item)

    def check_products(self):
        '''
        Check if there are at least one product name in selled db
        '''
        if not self.dbm.is_seller_product_exists():
            #self.add_product_widget.show()
            return False
        pass

    def add_product(self,product_name,product_price, product_number):
        print "SellerMainWindow::add_product",product_name,product_price,product_number
        
        try:
            self.dbm.add_product(self.seller_login,product_name,product_price,product_number)
            show_info("Product successfully added.")
        except Exception,e:
            show_info("Error occured. Product not added")
            print e
            self.close()
