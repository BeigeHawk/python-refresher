import numpy as np


class BankAccount:
    def __init__(self, name: str, account_number: int, balance: float):
        if self.balance < 0:
            print("Balance cannot be negative")
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def transaction(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def print(self, balance):
        print(f"Hello {self.name}, your balance is {self.balance}.")