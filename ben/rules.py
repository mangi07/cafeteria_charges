# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:03:35 2018

@author: Ben.Olson
"""

from decimal import *

class Stats:
    def __init__(self, mtype, amount, benefit=False, accompany=False):
        self.mtype = mtype
        self.amount = amount
        # boolean whether staff allowance applies
        self.is_benefit = benefit
        # some other condition that must be satisfied for benefit to apply,
        # such as whether other items must be ordered that day for the benefit to apply
        # 
        # Checker is responsible to know the condition and check based on condition
        self.must_be_accompanied = accompany
        
class Rules:
    def __init__(self):
        self.max_benefit = 3
        
        self.menu_items = {
                "Bacon": Stats("breakfast", 2),
                "Sausage": Stats("breakfast", 2),
                "Scrambled Eggs": Stats("breakfast", 1.5),
                "Fried Rice": Stats("breakfast", 1.5),
                "French Toast": Stats("breakfast", 1),
                "Pancake": Stats("breakfast", 1),
                "Fruit": Stats("breakfast", 1),
                "Yogurt": Stats("breakfast", 1),
                "Pop Tarts": Stats("breakfast", 1),
                "Boiled Eggs": Stats("breakfast", .5),
                
                # allowed lunch items in this group
                "Hot Lunch": Stats("lunch", 5, True),
                "K3-K5 Hot Lunch": Stats("lunch", 3, True),
                "Salad": Stats("lunch", 5, True),
                "Deli Sandwich": Stats("lunch", 3, True),
                "Chicken Nuggets": Stats("lunch", 2.5, True),
                "Hot Dog": Stats("lunch", 2, True),
                "French Fries": Stats("lunch", 2, True),
                "Rice": Stats("lunch", 1, True, True),
                
                "Chips": Stats("lunch", 1),
                "Tuna Sushi": Stats("lunch", 2.5),
                "Salmon Sushi": Stats("lunch", 2.5),
                "Musubi Sushi": Stats("lunch", 2.5),
                "Spam Musubi": Stats("lunch", 2.5),
                
                # allowed ala carte items in this group
                "Corn Dog": Stats("ala carte", 2, True),
                "Hamburger": Stats("ala carte", 2, True),
                "Fried Chicken": Stats("ala carte", 2.5, True),
                "Chili & Rice": Stats("ala carte", 3, True),
                "Chili and Rice": Stats("ala carte", 3, True),
                "Pizza": Stats("ala carte", 3, True),
                
                "Gatorade": Stats("drink", 2),
                "Bottled Aloe": Stats("drink", 1.5),
                "Bottled Water": Stats("drink", 1),
                "Canned Tea": Stats("drink", 1),
                "Mr. Brown": Stats("drink", 1),
                "Milk": Stats("drink", 1),
                "Juice": Stats("drink", 1),
                
                "Ice Pop": Stats("other", .5),
                "Sherbert Push Pop": Stats("other", 1),
                "Fruit Bar": Stats("other", 1.5),
                "Ice Cream Sandwich": Stats("other", 1.5),
                "Acacia Bowl": Stats("other", 8),
                
                "Carry Out Tray": Stats("other", .25),
                "NO ID CARD FEE": Stats("other", .5),
                "STAFF ALLOWANCE": Stats("other", self.max_benefit*-1)
        }
        
        

    def is_allowance_item(self, description):
        item = self._find_item(description)
        if item is not None:
            return item.is_benefit
        else:
            self._add_item_to_menu(description)
    
    def item_must_be_accompanied(self, description):
        item = self._find_item(description)
        if item is not None:
            return item.must_be_accompanied
        else:
            return self._get_bool("Does this item need to be accompanied for the benefit to apply? (y/n) ")
    
    def _find_item(self, description):
        for key in self.menu_items:
            if key in description:
                item = self.menu_items[key]
                return item
        print("Unable to find ", description, " in the list of known items.")
        
    def _add_item_to_menu(self, description):
        is_benefit = self._get_bool("\nIs this item a benefit? (y/n) ")
        if is_benefit:
            must_be_accompanied = self._get_bool(
                "\nDoes this item need to be accompanied for the benefit to apply? (y/n) ")
        else:
            must_be_accompanied = False
        mtype = self._get_option()
        amount = self._get_amount()
        self.menu_items[description] = Stats(mtype, amount, is_benefit, must_be_accompanied)
        return is_benefit
        
    
    # adapted from:
    # https://stackoverflow.com/questions/32616548/how-to-have-user-true-false-input-in-python
    def _get_bool(self, prompt):
        while True:
            try:
               return {"y":True,"n":False}[input(prompt).lower()]
            except KeyError:
               print("Invalid input please enter 'y' or 'n'!")
               
    def _get_option(self):
        prompt = "\nWhat type of item is this: (1) breakfast, (2) lunch, (3) ale carte, (4) drink, (5) other: "
        choice = 0
        while True:
            try:
                choice = int(input(prompt))
                if choice < 1 or choice > 5:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input please enter a number 1 through 5!")
        if choice == 1:
            mtype = "breakfast"
        elif choice == 2:
            mtype = "lunch"
        elif choice == 3:
            mtype = "ale carte"
        elif choice == 4:
            mtype = "drink"
        elif choice == 5:
            mtype = "other"
        return mtype
            
    def _get_amount(self):
        prompt = "\nWhat is the item's amount?"
        while True:
            try:
               choice = Decimal(input(prompt))
               break
            except ValueError:
               print("Invalid input please enter a number 1 through 4!")
            
           
    
    