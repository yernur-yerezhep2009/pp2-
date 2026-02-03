# ============================================================================
# TOPIC 6: Practical example - Bank Account
# ============================================================================

class BankAccount:
    """Bank Account class with multiple features"""
    interest_rate = 0.02  # Class variable
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance variable
        self.balance = balance  # Instance variable
    
    def deposit(self, amount):
        """Deposit money into account"""
        self.balance += amount
        print(f"{self.account_holder} deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
    
    def apply_interest(self):
        """Apply interest to account"""
        self.balance += self.balance * self.interest_rate
        print(f"Interest applied. New balance: ${self.balance:.2f}")

account = BankAccount("Eve", 1000)
account.deposit(500)
account.withdraw(200)
account.apply_interest()









