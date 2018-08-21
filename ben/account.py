# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:03:32 2018

@author: Ben.Olson
"""
class Transaction:
    def __init__(self, date, kind, amount):
        __slots__ = ['date', 'kind', 'amount']
        self.date = date
        self.kind = kind
        self.amount = amount
        

class Member:
    def __init__(self, name):
        __slots__ = ['name', 'charge', 'allowance']
        self.name = name
        self.record = []
        
    def add_record(self):
        self.record.append(Transaction(date, kind, amount))
        
        
class Account:
    def __init__(self, name, ID):
        __slots__ = ['name', 'ID', 'members']
        self.name = name
        self.ID = ID
        self.members = []
        
    def add_member(self, name):
        self.members.append(Member(name))
        
