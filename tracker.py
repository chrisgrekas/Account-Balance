import json
from collections import defaultdict
import matplotlib.pyplot as plt


class Transaction:
    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self) -> str:
        return f"Transaction(amount={self.amount}, category={self.category!r}, date={self.date!r})"

    def to_dict(self) -> dict:
        return {"amount": self.amount, "category": self.category, "date": self.date}

    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(data["amount"], data["category"], data["date"])


class InsufficientFundsError(Exception):
    pass


class User:
    def __init__(self, name: str, initial_balance: float):
        self.name = name
        self.balance = initial_balance
        self._income: list[Transaction] = []
        self._expenses: list[Transaction] = []

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, balance={self.balance})"

    @property
    def transactions(self) -> list[Transaction]:
        return self._income + self._expenses

    def deposit(self, transaction: Transaction) -> str:
        self.balance += transaction.amount
        self._income.append(transaction)
        return (
            f"Deposited {transaction.amount}. "
            f"Reason: {transaction.category}. "
            f"Date: {transaction.date}. "
            f"Balance: {self.balance}."
        )

    def withdraw(self, transaction: Transaction) -> str:
        if transaction.amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {transaction.amount}; balance is {self.balance}."
            )
        self.balance -= transaction.amount
        self._expenses.append(transaction)
        return (
            f"Withdrew {transaction.amount}. "
            f"Reason: {transaction.category}. "
            f"Date: {transaction.date}. "
            f"Balance: {self.balance}."
        )

    def get_balance(self) -> str:
        return f"{self.name}'s balance: {self.balance}"

    def get_transactions(self) -> list[Transaction]:
        return self.transactions

    def get_income(self) -> list[Transaction]:
        return list(self._income)

    def get_expenses(self) -> list[Transaction]:
        return list(self._expenses)

    def get_expenses_by_category(self) -> dict[str, float]:
        totals: dict[str, float] = defaultdict(float)
        for t in self._expenses:
            totals[t.category] += t.amount
        return dict(totals)

    def get_income_by_category(self) -> dict[str, float]:
        totals: dict[str, float] = defaultdict(float)
        for t in self._income:
            totals[t.category] += t.amount
        return dict(totals)

    def export_expenses(self, path: str = "expenses.json") -> None:
        _write_json(path, [t.to_dict() for t in self._expenses])

    def export_income(self, path: str = "incomes.json") -> None:
        _write_json(path, [t.to_dict() for t in self._income])

    def import_expenses(self, path: str = "expenses.json") -> str:
        for t in _read_json_transactions(path):
            self._expenses.append(t)
            self.balance -= t.amount
        return f"Balance after import: {self.balance}"

    def import_income(self, path: str = "incomes.json") -> str:
        for t in _read_json_transactions(path):
            self._income.append(t)
            self.balance += t.amount
        return f"Balance after import: {self.balance}"

    def plot_expenses(self) -> None:
        _bar_chart(self.get_expenses_by_category(), "Expenses by Category", "Category", "Amount")

    def plot_income(self) -> None:
        _bar_chart(self.get_income_by_category(), "Income by Category", "Category", "Amount")


def _write_json(path: str, data: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _read_json_transactions(path: str) -> list[Transaction]:
    with open(path, "r", encoding="utf-8") as f:
        return [Transaction.from_dict(item) for item in json.load(f)]


def _bar_chart(data: dict[str, float], title: str, xlabel: str, ylabel: str) -> None:
    plt.figure()
    plt.bar(list(data.keys()), list(data.values()))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
