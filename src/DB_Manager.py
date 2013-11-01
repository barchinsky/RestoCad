#!/usr/bin/env python

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Need to define logic for installation system at external system.
!!!!!!!!!!!!!!!!!!!!
'''

import sys

sys.path.append("/home/max/Documents/personal_stuff/study/RestoCad/")

import xml.etree.ElementTree as ET
from xml.dom import minidom
import time
import warnings
from lxml import etree

class DB_Manager:
    def __init__(self):
        
        self._seller_db = '../db/SELLER_DB_TEST.xml'

    def create_seller_db(self):
        db=open(self._seller_db,'w')
        
        root = ET.Element("root")

        sellers = ET.SubElement(root,"sellers")
        db.write( minidom.parseString(ET.tostring(root)).toprettyxml() )

    def remove_seller(self,seller_id):
        db = ET.parse(self._seller_db)
        root = db.getroot()

        for item in root.findall('sellers'):
            for seller in item:
                #print seller
                id = seller.find('id').text
                #print id
                if id == str(seller_id):
                    print "Record with id:%s will be removed"%str(seller_id)
                    item.remove(seller)

        #db.write( minidom.parseString(ET.tostring(root)).toprettyxml() )
        db.write(self._seller_db) 

    def add_seller(self,seller_id,login,password):
        if self.check_seller_unique(seller_id):
            db = ET.parse(self._seller_db)
            root = db.getroot()

            _sellers = root.find('sellers')

            _seller = ET.SubElement(_sellers,"seller")
            _id = ET.SubElement(_seller,'id')
            _id.text = str(seller_id)
            _login = ET.SubElement(_seller,'login')
            _login.text = login
            _password = ET.SubElement(_seller,'pass')
            _password.text = password
            _products = ET.SubElement(_seller,'products')
     
            db.write(self._seller_db)
        else:
            print "There is already seller with the same id.\nSeller not added."

    def check_seller_unique(self,id):
        '''
        Check if seller attended to register has unique attributes.
        '''
        db = ET.parse(self._seller_db)
        root = db.getroot()
        sellers = root.find('sellers')

        for seller in sellers:
            if seller.find('id').text == str(id):
                return False
        return True

    def add_product(self,seller_id,product_id,product_name,product_price,product_number):
        db = ET.parse(self._seller_db)

        root = db.getroot()

        sellers = root.find('sellers')

        if sellers is not None:
            for seller in sellers:
                id = seller.find('id').text
                if str(seller_id) == id:
                    print "Required seller found. Adding product to product list."
                    _products = seller.find('products')
                    _product = ET.SubElement(_products,'product')
                    _product_id = ET.SubElement(_product,'id')
                    _product_id.text=str(product_id)
                    _product_name = ET.SubElement(_product,'name')
                    _product_name.text = product_name
                    _product_price = ET.SubElement(_product,'price')
                    _product_price.text = product_price
                    _product_number_to_sell = ET.SubElement(_product,'product_number')
                    _product_number_to_sell.text = str(product_number)
                    db.write(self._seller_db)
        else:
            print 'No section section "sellers" in db. Can not add product. Check db structure.'

    def remove_product(self,seller_id,product_name):
        '''
        Remove product from seler db.
        '''
        print "Remove method called."
        db = ET.parse(self._seller_db)

        root = db.getroot()

        sellers = root.find('sellers')
        print sellers
        print sellers.findall('seller')

        if sellers is not None:
            for seller in sellers:
                products = seller.find('products')
                print products
                if products is not None:
                    for product in products:
                        if product.find('name').text == str(product_name):
                            print "Product found. Deletion will process..."
                else:
                    print "Error. Bad db structure."
                    return 0
        else:
            print "Error.Bad db structure. Product not removed."
            return 0

    def make_pretty(self):
        warnings.warn("This option is unsafe. Don't use it if you don't know what happend.")
        answer = raw_input("Do you want to continue?(y/n)")
        if answer == 'y':
            infile = open(self._seller_db,'r')
            data = infile.read()
            print data
            infile.close()

            root = etree.fromstring(data) # or xml.dom.minidom.parseString(xml_string)
            print etree.tostring(root,pretty_print=True)

            pretty_db = open(self._seller_db+str(int(time.time())),'w')
            pretty_db.write("")
            pretty_db.close()
            print "DB pretty print done."
        else:
            print "Good decsision. Bye!"

    def get_seler_product_list(self, seller_id):
        product_list = {}
        infile = open(self._seller_db,'r')
        data = infile.read()
        infile.close()

        root = ET.fromstring(data)

        sellers = root.find('sellers')

        for seller in sellers:
            if seller.find('id').text == str(seller_id):
                id = seller.find('id').text
                print "Required seller found: id=%s.\nProcessing data..."%id

                products = seller.find('products')

                for product in products:
                    product_id = product.find('id').text
                    product_name = product.find('name').text
                    product_price = product.find('price').text
                    product_number = product.find('product_number').text

                    product_list[product_name] = (product_id,product_price,product_number)

                    print 10*"-", '\n',product_id,product_name,product_price,product_number, '\n',10*"-"
        print "Finished."
        return product_list

if __name__ == "__main__":
    dbm = DB_Manager()
    #dbm.remove_seller(2)
    dbm.add_seller(1,"max","pass")
    dbm.add_product(seller_id=1,product_id=2,product_name='icecream2',product_price='1.5', product_number=100)

    #dbm.make_pretty()
    seller = dbm.get_seler_product_list(1)
    print seller
    #dbm.remove_product(seller_id=1,product_name='icecream2')
