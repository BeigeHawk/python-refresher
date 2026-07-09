import numpy as np


class BankAccount:
    def __init__(self, name: str, account_number: int, balance: float):
        if self.balance < 0:
            raise ValueError("Balance cannot be negative")
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount to withdraw must be a positive number")
        if amount > self.balance:
            raise ValueError("You have insufficient funds")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount to deposit must be a positive number")
        self.balance += amount
        return self.balance

    def print_balance(self):
        balance_message = f"Hello {self.name}, the balance for account {account_number} is {self.balance}."
        print(balance_message)
        return balance_message