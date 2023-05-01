from .bank import BankAccount, TransactionType
import pytest


@pytest.mark.parametrize("type, amount, to, expected", [
    (TransactionType.FUND.value, 1000, "ACC-53635273637237263", 4000),
    (TransactionType.PAYMENT.value, 4800, "ACC-53635273637237263", 200),
    (TransactionType.FUND.value, 2000, "ACC-53635273637237263", 3000),
    (TransactionType.PAYMENT.value, 5000, "ACC-53635273637237263", 0),
])
def test_can_make_transaction(account, type, amount, to, expected):
    assert account.make_transaction(type, amount, to) == expected
