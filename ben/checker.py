# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:20:16 2018

@author: Ben.Olson
"""

"""TODO: For each account:
    For each member go through their records for each day to create a Day object:
        For each record, accumulate amounts into the following properties:
            1. total amount ordered that is eligible for benefit
            2. total amount ordered
            3. total benefits applied
            4. total amount charged
            
            Calculate what the amounts should be.
            Compare expected with actual for benefits.
            Note amount benefit should change to if needed.
            
    Compare expected and actual total for the account.
    Change total for that account if needed.
    
    **May want to write to excel as you go.
"""

import ben.rules
from ben.account import Record

class Day:
    def __init__(self, records=None):
        __slots__ = ['records', 'benefit_amount', 'total', 'expected_total']
        if records is None:
            records = []
        self.records = records
        self.benefit_amount = 0
        self.total = 0
        self.expected_total = 0

class Checker:
    def __init__(self, accounts):
        self.accounts = accounts
        self.rules = ben.rules.Rules()
        
    def check(self):
        for key in self.accounts:
            account = self.accounts[key]
            self.check_members(account)
        self.check_account_totals(self.accounts)
            
    def check_members(self, acct):
        for member_key in acct.members:
            member = acct.members[member_key]
            days = {}
            for record in member.records:
                if record.date not in days:
                    days[record.date] = Day()
                day = days[record.date]
                day.records.append(record)
                self.debug_days(days)
            self.check_days(days, member)
            for k, v in days.items():
                v.records.clear()
                
    def debug_days(self, days):
        print("\n*****")
        for k, v in days.items():
            print("day: ", k)
            for r in v.records:
                print("**record: ", r)
    
    # check one member, where each Day in days contains a list of his/her records
    def check_days(self, days, member):
        """for each day, get expected benefit"""
        for key in days:
            #print("Number of records for ", key, ": ", len(days[key].records))
            daily_benefit = 0
            total_charges = 0
            total_balance = 0
            total_eligible = 0
            part_of_eligible = 0
            benefit_records = []
            
            # go through records for one day
            for record in days[key].records:
                #print("day key: ", key)
                total_balance += record.amount
                if record.amount < 0:
                    daily_benefit += abs(record.amount)
                    benefit_records.append(record)
                else:
                    total_charges += record.amount
                    
                if ( self.rules.is_allowance_item(record.description) 
                        and not self.rules.item_must_be_accompanied(record.description)
                        and record.amount > 0 ):
                    total_eligible += record.amount
                # need to account for items that (must be accompanied for benefit to apply)
                if ( self.rules.item_must_be_accompanied(record.description)
                        and record.amount > 0 ):
                    part_of_eligible += record.amount
                    total_eligible += record.amount

            if part_of_eligible >= total_eligible:
                total_eligible = 0
            if total_eligible > abs(self.rules.max_benefit):
                total_eligible = abs(self.rules.max_benefit)
            if daily_benefit < abs(total_eligible):
                # then too little benefit was given that day
                benefit = daily_benefit - total_eligible
                new_record = Record(key, "ADD MISSING BENEFIT", benefit)
                new_record.updated_amount = benefit
                member.records.append(new_record)
            if daily_benefit > abs(total_eligible):
                # then too much benefit was given that day and we need to take back the difference
                take_back = daily_benefit - total_eligible
                for benefit in benefit_records:
                    benefit.updated_amount = (abs(benefit.amount) - take_back) * -1
                    #print("*daily_benefit: ", daily_benefit)
                    #print("**total_eligible: ", total_eligible)
                    #print("benefit.updated_amount: ", benefit.updated_amount)
                    break
                
                
    def check_account_totals(self, accts):
        """for each account, add up each day's expected total
        and add to the account expected total"""
        for key in accts:
            acct = accts[key]
            #acct.expected_total = acct.total
            acct.expected_total = 0
            for key in acct.members:
                for record in acct.members[key].records:
                    if record.updated_amount is not None:
                        #difference = record.amount - record.updated_amount
                        #acct.expected_total = acct.expected_total - difference
                        acct.expected_total += record.updated_amount
                    else:
                        acct.expected_total += record.amount

    
    
    
    
    
    
    
    