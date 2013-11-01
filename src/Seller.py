#!/usr/bin/env python

import sys
sys.path.append("/home/max/Documents/personal_stuff/study/src/db_manager")
from DB_Manager import DB_Manager

class Seller:
    def __init__(self,id,login,password):
        self._dbm = DB_Manager()
        self._id = id
        self._login = login
        self._password = password

        self._product_list={} # product_id - product_name
        self._price_list = {}

        self.load()

    def load(self):
        '''
        Read data from db about seller.
        '''
        self._product_list = self._dbm.get_seler_product_list(self._id)

    def get_id(self):
        return self._id

    def get_product_id(self, product):
        pass

    def get_price_list(self):
        return self._price_list

    def add_product(self,product_id,product_name,product_price,product_number):
        '''
        Logic to add product to db
        '''
        self._dbm.add_product(seller_id=self._id, product_id=2, product_name, product_price, product_number)

    def get_product_list(self):
        return self._product_list


################################## DEBUG ######################################
if __name__ == "__main__":
    sell = Seller(1,login="max", password="pass")
