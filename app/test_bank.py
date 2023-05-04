from .bank import TransactionType
import pytest


@pytest.mark.parametrize("type, amount, to, expected", [
    (TransactionType.FUND.value, 1000, "ACC-53635273637237263", 4000),
    (TransactionType.PAYMENT.value, 4800, "ACC-53635273637237263", 200),
    (TransactionType.FUND.value, 2000, "ACC-53635273637237263", 3000),
    (TransactionType.PAYMENT.value, 5000, "ACC-53635273637237263", 0),
])
def test_can_make_transaction(account, type, amount, to, expected):
    assert account.make_transaction(type, amount, to) == expected


@pytest.mark.parametrize("type, amount, to", [
    (TransactionType.FUND.value, 8000, "ACC-53635273637237263"),
    (TransactionType.PAYMENT.value, 14000, "ACC-53635273637237263"),

])
def test_make_transaction_can_raise_error(account, type, amount, to):
    """
    Testing whether make_transaction can raise an error
    when amount is greater than the balance
    """
    with pytest.raises(ValueError):
        account.make_transaction(type, amount, to)
