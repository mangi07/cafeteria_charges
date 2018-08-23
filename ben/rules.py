# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:03:35 2018

@author: Ben.Olson
"""

class Stats:
    def __init__(self, mtype, amount, benefit=False, conditional=False):
        self.mtype = mtype
        self.amount = amount
        # boolean whether staff allowance applies
        self.benefit = benefit
        # whether other items must be ordered that day for the benefit to apply
        self.conditional = conditional
        
class Rules:
    def __init__(self):
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
                "Samon Sushi": Stats("lunch", 2.5),
                "Musubi Sushi": Stats("lunch", 2.5),
                "Spam Musubi": Stats("lunch", 2.5),
                
                # allowed ala carte items in this group
                "Corn Dog": Stats("ala carte", 2, True),
                "Hamburger": Stats("ala carte", 2, True),
                "Fried Chicken": Stats("ala carte", 2.5, True),
                "Chili & Rice": Stats("ala carte", 3, True),
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
                "NO ID CARD FEE": Stats("other", .5)
        }

    def is_allowance_item(self, description):
        for item in self.menu_items:
            if item in description:
                return True
        return False