import unittest
from ben.checker import Checker
from ben.checker import Day
from ben.account import Record
from datetime import datetime

"""
https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/

cd to project root and run tests with:
python -m unittest discover -v
"""
class TestChecker(unittest.TestCase):

    checker = None
    days = None
    accts = None

    def setUp(self):
        self.accts = None
        self.day1 = datetime(2018, 8, 27)
        self.day2 = datetime(2018, 8, 28)
        self.day3 = datetime(2018, 9, 1)
        self.day4 = datetime(2018, 9, 30)
        self.day5 = datetime(2018, 10, 2)
        self.day6 = datetime(2018, 10, 3)

        self.checker = Checker(self.accts) # self.accts never used but needed to create object here
        self.days = {
            # expect second record updated_amount to change to 0
            self.day1: Day([Record(self.day1, "Cash Register - Chips", 1),
                    Record(self.day1, "Cash Register - STAFF ALLOWANCE", -3)]),

            # expect second record updated_amount to remain None
            self.day2: Day([Record(self.day2, "Cash Register - Hot Lunch", 5),
                   Record(self.day2, "Cash Register - STAFF ALLOWANCE", -3)]),

            # expect second record updated_amount to change to 3
            self.day3: Day([Record(self.day3, "Cash Register - Hot Lunch", 5),
                   Record(self.day3, "Cash Register - STAFF ALLOWANCE", -3),
                   Record(self.day3, "Cash Register - STAFF ALLOWANCE", -3),
                   Record(self.day3, "Cash Register - STAFF ALLOWANCE", -3)]),

            # expect fourth record updated_amount to change to 0 (no benefit since rice was the only thing that day
            self.day4: Day([Record(self.day4, "Cash Register - Rice", 1),
                            Record(self.day4, "Cash Register - Rice", 1),
                            Record(self.day4, "Cash Register - Rice", 1),
                            Record(self.day4, "Cash Register - STAFF ALLOWANCE", -3)]),

            # expect fourth record updated_amount to change to 0
            # (still no benefit since no other eligible items were ordered that day)
            self.day5: Day([Record(self.day5, "Cash Register - Rice", 1),
                            Record(self.day5, "Cash Register - Gatorade", 1),
                            Record(self.day5, "Cash Register - Boiled Eggs", 1),
                            Record(self.day5, "Cash Register - STAFF ALLOWANCE", -3)]),

            # expect fourth record to not be updated since rice ordered with eligible item Fried Chicken
            self.day6: Day([Record(self.day6, "Cash Register - Rice", 1),
                            Record(self.day6, "Cash Register - Fried Chicken", 2.50),
                            Record(self.day6, "Cash Register - Boiled Eggs", 1),
                            Record(self.day6, "Cash Register - STAFF ALLOWANCE", -3)])
        }

    def test_checkDays(self):
        self.checker.check_days(self.days)
        self.assertTrue(self.days[self.day1].records[1].updated_amount == 0)
        self.assertTrue(self.days[self.day2].records[1].updated_amount == None)
        self.assertTrue(self.days[self.day3].records[1].updated_amount == 3)
        self.assertTrue(self.days[self.day4].records[3].updated_amount == 0)
        self.assertTrue(self.days[self.day5].records[3].updated_amount == 0)
        self.assertTrue(self.days[self.day6].records[3].updated_amount == None)


if __name__ == '__main__':
    unittest.main()