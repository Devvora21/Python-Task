class InsufficientFundsError(Exception):
    pass

class InvalidDepositError(Exception):
    pass

class BankAccount:
    def __init__(self, account_holder_name, balance=0.0):
        self.account_holder_name = account_holder_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidDepositError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Account Balance: ${self.balance}")
        return self.balance


try:
    account = BankAccount("Dev Vora", 500)
    account.deposit(200)
    account.withdraw(100)
    account.withdraw(700)  # This should raise an InsufficientFundsError
except (InsufficientFundsError, InvalidDepositError, ValueError) as e:
    print(f"Error: {e}")
