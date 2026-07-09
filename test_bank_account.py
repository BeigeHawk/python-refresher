import unittest
import bank_account
import numpy as np


class TestAccount(unittest.TestCase):
    bank_account.name = str("Noah")
    bank_account.account_number = 123456
    bank_account.balance = 100.00

    def test_initial_balance(bank_account):
        bank_account.assertEqual(bank_account.balance, 100)

    def test_withdraw(self):
        self.assertEqual(bank_account.withdraw(10), 90)