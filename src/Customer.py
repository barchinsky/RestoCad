#!/usr/bin/env python

class Customer:
    def __init__(self,id):
        self._id = id

        customer_db_name = "Customer_"+self._id
        db = open(customer_db_name,'w')

    def registration(self,login,password):
        try:
            db.write(self._id+','+login+',',password)
            return 1
        except Exception, e:
            raise "Registration failed."+str(e)
            return 0
    
    def set_current_location(self, location):
        pass

    def order_place(self, restoran, place):
        pass

    def get_free_places(self,restoran):
        pass

    def load_data(self):
        '''
        Load data from db about customer.
        '''
        pass

