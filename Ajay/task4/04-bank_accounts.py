import unittest

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        return self.balance * self.interest_rate / 100
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than the available balance in SavingsAccount")
        super().withdraw(amount)
        
class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Cannot withdraw more than the available balance in CheckingAccount")
        self.balance -= amount
         
# Unit Tests
class TestBankAccounts(unittest.TestCase):
    def test_savings_account(self):
        savings = SavingsAccount(1001, 1000, 5)  # Interest rate in percentage
        self.assertEqual(savings.calculate_interest(), 50)  # Correct interest amount
        savings.withdraw(500)
        self.assertEqual(savings.balance, 500)
        with self.assertRaises(ValueError):
            savings.withdraw(1000)
    
    def test_checking_account(self):
        checking = CheckingAccount(2001, 1000, 200)
        checking.withdraw(1100)  # Overdraft used
        self.assertEqual(checking.balance, -100)
        with self.assertRaises(ValueError):
            checking.withdraw(300)  # Exceeds overdraft limit

if __name__ == "__main__":
    unittest.main()
