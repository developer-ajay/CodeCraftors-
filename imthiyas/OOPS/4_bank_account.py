"""
4. Medium: Create a class hierarchy for a banking system with a base class 'Account' 
and derived classes 'SavingsAccount' and 'CheckingAccount'.
- Account should have balance and account_number
- SavingsAccount should have interest_rate and calculate_interest() method
- CheckingAccount should have overdraft_limit
Both derived classes should override withdraw() method with their specific rules.
"""
import unittest
import math
class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            return True
        return False
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return True
        return False        

class SavingsAccount(Account):
    def __init__(self, account_number, balance,interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        return super().withdraw(amount)

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Exceeded overdraft limit")
        self.balance -= amount
        return True

class TestBankAccounts(unittest.TestCase):
    def test_savings_account(self):
        savings = SavingsAccount(1001, 1000, 0.05)
        self.assertEqual(savings.calculate_interest(), 50)
        savings.withdraw(500)
        self.assertEqual(savings.balance, 500)
        with self.assertRaises(ValueError):
            savings.withdraw(1000)
    
    def test_checking_account(self):
        checking = CheckingAccount(2001, 1000, 200)
        checking.withdraw(1100)
        self.assertEqual(checking.balance, -100)
        with self.assertRaises(ValueError):
            checking.withdraw(300)

if __name__ == "__main__":
    unittest.main()