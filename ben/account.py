# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:03:32 2018

@author: Ben.Olson
"""
class Record:
    def __init__(self, date, description, amount):
        __slots__ = ['date', 'description', 'amount']
        self.date = date
        self.description = description
        self.amount = amount
        

class Member:
    def __init__(self, name):
        __slots__ = ['name']
        self.name = name
        self.record = {}
        
    def add_record(self, date, descr, amount):
        self.record.append(Record(date, descr, amount))
        
        
class Account:
    def __init__(self, name, ID):
        __slots__ = ['name', 'ID', 'members']
        self.name = name
        self.ID = ID
        self.members = {}
        
    def add_member(self, name):
        self.members[name] = Member(name)
        
