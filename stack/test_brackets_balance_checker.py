import imp
from unittest import TestCase
from brackets_balance_checker import check_brackets_balance

class TestBalanceChecker(TestCase):
    def test_checker(self):
        self.assertEqual(check_brackets_balance("(())"), True)
        self.assertEqual(check_brackets_balance("(())"), True)
        self.assertEqual(check_brackets_balance("())("), False)
        self.assertEqual(check_brackets_balance("))(("), False)
        self.assertEqual(check_brackets_balance("((())"), False)
        self.assertEqual(check_brackets_balance("(()((())()))"), True)
        self.assertEqual(check_brackets_balance("(()((())()))"), True)
        self.assertEqual(check_brackets_balance("(()()(()"), False)
    
