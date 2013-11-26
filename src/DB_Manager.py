#!/usr/bin/env python

import sys

sys.path.append("/home/max/Documents/personal_stuff/study/RestoCad/")

import xml.etree.ElementTree as ET
from xml.dom import minidom
import time
import warnings
from lxml import etree

class DB_Manager:
    def __init__(self):
        
        self._database = '../db/DB_TEST.xml'

    def create_db(self):
        db=open(self._database,'w')
        
        root = ET.Element("root")

        sellers = ET.SubElement(root,"sellers")
        customers = ET.SubElement(root,"customers")
        restorators = ET.SubElement(root,"restorators")
        db.write( minidom.parseString(ET.tostring(root)).toprettyxml() )

    def remove_user(self,user_group,user_login):
        db = ET.parse(self._database)
        root = db.getroot()
        user_group = root.find(user_group+'s')

        for user in user_group:
            print "User:",user
            login = user.find('login').text
            print login
            if login == str(user_login):
                print "Record with login:%s will be removed"%str(user_login)
                user_group.remove(user)

        #db.write( minidom.parseString(ET.tostring(root)).toprettyxml() )
        db.write(self._database) 


    def add_user(self,user_type,login,password):
        try:
            db = ET.parse(self._database)
            root = db.getroot()

            _user_group = root.find(user_type+'s')
            print _user_group
            print user_type
            _user = ET.SubElement(_user_group,user_type)
            print _user

            _login = ET.SubElement(_user,'login')
            _login.text = login
            _password = ET.SubElement(_user,'pass')
            _password.text = password

            db.write(self._database)
        except Exception,e:
            print "DB_Manager::add_user()::"+str(e)

    def add_restorator(self,login,password,restoran_name,restoran_location, places_count):
        db = ET.parse(self._database)
        root = db.getroot()
 
        _restorators = root.find('restorators')
        _restorator = ET.SubElement(_restorators,"restorator")
        _id = ET.SubElement(_restorator,'id')
        _login = ET.SubElement(_restorator,'login')
        print login
        _login.text = login
        _password = ET.SubElement(_restorator,'pass')
        _password.text = password
        _restoran_name = ET.SubElement(_restorator,'restoran_name')
        _restoran_name.text = restoran_name
        _restoran_location = ET.SubElement(_restorator,'restoran_location')
        _restoran_location.text = restoran_location
        _places_count = ET.SubElement(_restorator,'places_count')
        _grade = ET.SubElement(_restorator,'grade')
        _grade.text = '0'
        _places_count.text = places_count
        
        db.write(self._database)

    def check_unique(self,user_type,user_name):
        '''
        Check if seller attended to register has unique attributes.
        '''
        print "Check unique method."
        print user_type,user_name

        db = ET.parse(self._database)
        root = db.getroot()
        user_group = root.find(user_type+'s')

        for user in user_group:
            if user.find('login').text == user_name:
                print "There is such user in system."
                return False

        print "User is unique."
        return True

    def find_user_for_authorization(self,user_type, login, password):
        print "Find user for authorization."
        infile = open(self._database,'r')
        data = infile.read()
        infile.close()

        root = ET.fromstring(data)

        user_group = root.find(user_type+'s')

        for user in user_group:
            print 'User:',user
            if user.find('login').text == login and user.find('pass').text == password:
                print "Found!"
                return True
        return False

    def add_product(self,seller_id,product_id,product_name,product_price,product_number):
        db = ET.parse(self._database)

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
                    db.write(self._database)
        else:
            print 'No section section "sellers" in db. Can not add product. Check db structure.'

    def remove_product(self,seller_id,product_name):
        '''
        Remove product from seler db.
        '''
        print "Remove method called."
        db = ET.parse(self._database)

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

    def modify_product_data(self, seler_id, product_id, attribute_to_modify, value):
        pass

    def make_pretty(self):
        warnings.warn("This option is unsafe. Don't use it if you don't know what happend.")
        answer = raw_input("Do you want to continue?(y/n)")
        if answer == 'y':
            infile = open(self._database,'r')
            data = infile.read()
            print data
            infile.close()

            root = etree.fromstring(data) # or xml.dom.minidom.parseString(xml_string)
            print etree.tostring(root,pretty_print=True)

            pretty_db = open(self._database+str(int(time.time())),'w')
            pretty_db.write("")
            pretty_db.close()
            print "DB pretty print done."
        else:
            print "Good decsision. Bye!"

    def get_seller_product_list(self, seller_id):
        product_list = {}
        infile = open(self._database,'r')
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

    def get_restoran_list(self):
        restoran_list = []
        data = ""

        with open(self._database,'r') as f:
            data = f.read()
            f.close()
        
        root = ET.fromstring(data)

        restorators = root.find("restorators")

        if restorators is not None:
            for restorator in restorators:
                restoran_list.append( restorator.find("restoran_name").text )
        else:
            print "No restoran found."
            return False
        return restoran_list
    
    def get_restoran_menu(self,restoran):
        print "Fake method"
        if restoran == "The One":
            return ["dish1","dish2"]
        else:
            return ["dish3","dish4"]

    def get_restoran_location(self,restoran):
        data = self.get_db()

        root = ET.fromstring(data)

        restorators = root.find("restorators")

        if restorators is not None:
            for restorator in restorators:
                if restorator.find("restoran_name").text == restoran:
                    return ( restorator.find("restoran_location").text )
        else:
            return None

    def get_restoran_grade(self,restoran):
        data = self.get_db()
        root = ET.fromstring(data)
        restorators = root.find("restorators")

        if restorators is not None:
            for restorator in restorators:
                if restorator.find("restoran_name").text == restoran:
                    return restorator.find("grade").text if restorator.find("grade").text is not None else 0 

    def set_restoran_grade(self,restoran,grade,visit_date="test_date"):
        db = ET.parse(self._database)
        root = db.getroot()

        restorators = root.find("restorators")

        for restorator in restorators:
            if restorator.find("restoran_name").text == restoran:
                print "Current restoran grade:", restorator.find("grade").text #= str( int(restoran.find("grade").text) + int(grade) ) # update grade
                restorator.find("grade").text = str( int(restorator.find("grade").text) + int(grade) ) # update grade

        db.write(self._database)

    def get_free_places_number(self,restoran):
        print "get_free_places_number::name goted%s"%restoran
        data = self.get_db()
        root = ET.fromstring(data)
        restorators = root.find("restorators")

        if restorators is not None:
            for restorator in restorators:
                if restorator.find("restoran_name").text == restoran:
                    return restorator.find("places_count").text if int( restorator.find("places_count").text ) > 0 else 0 
                    print "olo"
                    return "Olo"
  
    def update_free_places(self,restoran,op=0):
        db = ET.parse(self._database)
        root = db.getroot()

        restorators = root.find("restorators")

        for restorator in restorators:
            if restorator.find("restoran_name").text == restoran:
                print "Restoran found!"
                if op: # increase place count
                    restorator.find("places_count").text = str( int(restorator.find("places_count").text) + 1 )
                else: # decrease
                    restorator.find("places_count").text = str( int(restorator.find("places_count").text) - 1 )

        db.write(self._database)


    def get_db(self):
        with open(self._database) as f:
            return f.read()

 
    
            

if __name__ == "__main__":
    dbm = DB_Manager()
    #dbm.create_db()
    #dbm.remove_user('customer','test_customer')
    #dbm.add_seller("max","pass")
    #dbm.add_customer('test_customer','pass')
    #dbm.add_product(seller_id=1,product_id=2,product_name='icecream2',product_price='1.5', product_number=100)

    #dbm.make_pretty()
    #seller = dbm.get_seler_product_list(1)
    #print seller
    #dbm.remove_product(seller_id=1,product_name='icecream2')

    #dbm.find_user_for_authorization('seller','max','pass')
    #dbm.check_unique("seller","max2")
    #dbm.add_user("customer","max3","test")
    #dbm.add_user('restorator','r1','r1234')
    #print dbm.get_restoran_list()
