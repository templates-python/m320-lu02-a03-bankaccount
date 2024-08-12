import pytest
from bank_account import BankAccount
# Annahme: Die BankAccount-Klasse ist in einer Datei namens 'bank_account.py' definiert

class TestBankAccount:

    @pytest.fixture
    def new_account(self):
        return BankAccount(1000, 'John Doe')

    def test_initial_balance(self, new_account):
        assert new_account.balance == 0.0

    def test_initial_overdraft(self, new_account):
        assert new_account.overdraft == 1000

    def test_customer(self, new_account):
        assert new_account.customer == 'John Doe'

    def test_booking(self, new_account):
        new_account.booking(500)
        assert new_account.balance == 500

    def test_get_money_available(self, new_account):
        new_account.booking(1000)
        amount = new_account.get_money(800)
        assert amount == 800
        assert new_account.balance == 200

    def test_get_money_not_available(self, new_account):
        new_account.booking(500)
        amount = new_account.get_money(2000)
        assert amount == 0.0
        assert new_account.balance == 500

    def test_get_money_overdraft(self, new_account):
        new_account.booking(500)
        amount = new_account.get_money(1300)
        assert amount == 1300  # Max overdraft limit
        assert new_account.balance == -800

    def test_balance_after_transactions(self, new_account):
        new_account.booking(1000)
        new_account.get_money(800)
        assert new_account.balance == 200