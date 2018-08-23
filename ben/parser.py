# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:50:11 2018

@author: Ben.Olson
"""
import re
import datetime
from enum import Enum
from ben.account import *

class Kind(Enum):
        FAMILY_NAME = 1
        DATE = 2
        FAMILY_MEMBER = 3
        AMOUNT = 4
        OTHER = 5


class Parser:
    
    def __init__(self):
        self.accts = {}
        self.curr_acct = None
        self.curr_member = None
        
        self.temp_date = None
        self.temp_member_name = None
        self.temp_amount = None
        self.temp_record_descr = None
        self.prev_cell = None
    
        # Example match: "LastA, FirstA and LastB, FirstB (123)"
        # group 0: "LastA, FirstA and LastB, FirstB (123)"
        # group 1: "LastA, FirstA and LastB, FirstB"
        # group 2: "123"
        self.family_name_pattern = re.compile(r"([a-zA-Z 0-9]+, [a-zA-Z ,0-9]+) \(([0-9]+)\)")
        self.member_pattern = re.compile(r"[a-zA-Z 0-9]+, [a-zA-Z 0-9]+")
        
    
    def determine_kind(self, cell_value):
        if type(cell_value) == int or type(cell_value) == float:
            return Kind.AMOUNT
        elif type(cell_value) == str:
            name = self.family_name_pattern.match(cell_value)
            if name:
                return Kind.FAMILY_NAME
            name = self.member_pattern.match(cell_value)
            if name:
                return Kind.FAMILY_MEMBER
            return Kind.OTHER
        elif type(cell_value) == datetime.datetime:
            return Kind.DATE
    
    
    def gather_data(self, cell_value, row, col):
        kind = self.determine_kind(cell_value)
        if kind == Kind.FAMILY_NAME:
            if cell_value in self.accts:
                self.curr_acct = self.accts[cell_value]
            else:
                ID = self.family_name_pattern.match(cell_value).group(2)
                acct = Account(cell_value, ID)
                self.accts[cell_value] = acct
                self.curr_acct = acct
        elif self.curr_acct is None:
            return
        elif kind == Kind.DATE:
            self.temp_date = cell_value
        elif kind == Kind.FAMILY_MEMBER:
            self.temp_member_name = cell_value
        elif kind == Kind.AMOUNT and self.prev_cell != "Total":
                # gather final cell in row and add a member's record
                self.temp_amount = cell_value
                if self.temp_member_name not in self.curr_acct.members:
                    self.curr_acct.add_member(self.temp_member_name)
                self.curr_acct.members[self.temp_member_name].add_record(
                        self.temp_date, 
                        self.temp_record_descr, 
                        self.temp_amount)
        elif kind == Kind.OTHER and col == 2:
            # record description expected in Excel column 2
            self.temp_record_descr = cell_value
        
        self.prev_cell = cell_value
        
    def get_account_data(self):
        return self.accts
    
    def print_account_data(self):
        for acct_key in self.accts:
            acct = self.accts[acct_key]
            print("\n\nAccount: ", acct.name, "ID: ", acct.ID)
            for member_key in acct.members:
                member = acct.members[member_key]
                print("****Member: ", member.name)
    
    
    
    
    