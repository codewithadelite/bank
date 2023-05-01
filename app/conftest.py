import pytest
from .bank import BankAccount, TransactionType


@pytest.fixture
def account() -> BankAccount:
    account = BankAccount(5000)
    return account
