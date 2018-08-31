import unittest
from ben.rules import Rules

"""
https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/

cd to project root and run tests with:
python -m unittest discover -v
"""
class TestRules(unittest.TestCase):

    rules = None
    
    
    def setUp(self):
        self.rules = Rules()
        
    def test_isAllowanceItem(self):
        #rules = Rules()
        result = self.rules.is_allowance_item("Cash Register - Hot Lunch")
        self.assertTrue(result)
    
    def test_isNotAllowanceItem(self):
        result = self.rules.is_allowance_item("Cash Register - Chips")
        self.assertFalse(result)
        
    def test_itemHasCondition(self):
        result = self.rules.item_must_be_accompanied("Cash Register - Rice")
        self.assertTrue(result)
        
    def test_itemDoesNotHaveCondition(self):
        result = self.rules.item_must_be_accompanied("Cash Register - K3-K5 Hot Lunch")
        self.assertFalse(result)
        
    def test_findItem(self):
        key, item = self.rules._find_item("Chili & Rice")
        self.assertTrue( key == "Chili & Rice" )
        key, item = self.rules._find_item("Chili and Rice")
        self.assertTrue( key == "Chili and Rice" )
        key, item = self.rules._find_item("Rice")
        self.assertTrue( key == "Rice" )
        
        key = None
        item = None
        key, item = self.rules._find_item("Chili")
        self.assertTrue( key == None )
        self.assertTrue( item == None )
        
        

if __name__ == '__main__':
    unittest.main()