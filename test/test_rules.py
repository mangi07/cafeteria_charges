import unittest
from ben.rules import Rules

"""
https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
"""
class TestRules(unittest.TestCase):

    def test_isAllowanceItem(self):
        rules = Rules()
        result = rules.is_allowance_item("Cash Register - Hot Lunch")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()