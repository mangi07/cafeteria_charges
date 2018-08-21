# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:50:11 2018

@author: Ben.Olson
"""
import re
import datetime
from enum import Enum


move_to_next_account = False

# Example match: "LastA, FirstA and LastB, FirstB (123)"
# group 0: "LastA, FirstA and LastB, FirstB (123)"
# group 1: "LastA, FirstA and LastB, FirstB"
# group 2: "123"
family_name_pattern = re.compile(r"([a-zA-Z 0-9]+, [a-zA-Z ,0-9]+) \(([0-9]+)\)")
member_pattern = re.compile(r"[a-zA-Z 0-9]+, [a-zA-Z 0-9]+")


class Kind(Enum):
    FAMILY_NAME = 1
    DATE = 2
    FAMILY_MEMBER = 3
    AMOUNT = 4
    OTHER = 5
    

def determine_kind(cell_value):
    if type(cell_value) == int or type(cell_value) == float:
        return Kind.AMOUNT
    elif type(cell_value) == str:
        name = family_name_pattern.match(cell_value)
        if name:
            return Kind.FAMILY_NAME
        name = member_pattern.match(cell_value)
        if name:
            return Kind.FAMILY_MEMBER
        return Kind.OTHER
    elif type(cell_value) == datetime.datetime:
        return Kind.DATE

def gather_data(cell_value):
    kind = determine_kind(cell_value)
    if kind == Kind.FAMILY_NAME:
        #print("family name: ", cell_value)
        pass
    elif kind == Kind.DATE:
        pass
    elif kind == Kind.FAMILY_MEMBER:
        #print("family member", cell_value)
        pass
    elif kind == Kind.AMOUNT:
        pass
    elif kind == Kind.OTHER:
        print("other: ", cell_value)
    
    
    
    
    