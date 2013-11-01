#!/usr/bin/env python

class Dish:
    def __init__(self,id,dish_name,ingredients):
        self._id = id
        self._dish_name = dish_name
        self._ingredients = []

        self._dish_file_name = "Dish_"+self._dish_name
        self._dish_file = open("../data/dishes/"+self._dish_file_name)

    def get_ingredients(self):
        return self._ingredients

    def add_ingredients(self,ingredient):
        self._ingredients.append(ingredient)
