"""
Modeule that contains codes to do bank processes
"""
from dataclasses import dataclass
from typing import List
from enum import Enum, auto


class TransactionType(Enum):
    PAYMENT = auto()
    FUND = auto()


@dataclass
class Transaction:
    type: TransactionType
    amount: int
    to: str


class BankAccount:
    """
        Contains methods to handle payment transfers
    """

    def __init__(self, balance: int) -> None:
        self.balance = balance
        self.transactions: List[Transaction] = []

    def make_transaction(self, type: TransactionType, amount: int, to: str) -> None:
        """
        Its transfers money to the person passed as argument

        Args:
            type: (TransactionType) The transaction type which specify the reason of transfer
            amount: (int) The amount to be transfered
            to: (str) The account number where to send money to

        Returns:
            None
        """
        if amount > self.balance:
            raise ValueError("You dont have enough balance.")
        self.balance -= amount
        transaction_data: Transaction = {
            "type": type,
            "amount": amount,
            "to": to
        }
        self.transactions.append(transaction_data)

    @property
    def get_current_balance(self) -> int:
        return self.balance

    @property
    def get_transactions(self) -> List[Transaction]:
        return self.transactions
