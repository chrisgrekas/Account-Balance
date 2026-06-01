from tracker import User, Transaction, InsufficientFundsError
from datetime import datetime


def create_transaction() -> Transaction:
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Enter a number.")
    category = input("Category: ")
    return Transaction(amount, category, now)


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a number.")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number.")


name = input("Name: ")
balance = get_float("Starting balance: ")
user = User(name, balance)

action = get_int("1 Transaction  2 Balance  3 Import income  4 Import expenses\n> ")
while action in [1, 2, 3, 4]:
    if action == 1:
        t = create_transaction()
        mode = get_int("1 Deposit  2 Withdraw\n> ")
        if mode == 1:
            print(user.deposit(t))
        elif mode == 2:
            try:
                print(user.withdraw(t))
            except InsufficientFundsError as e:
                print(e)
        else:
            print("Invalid.")
    elif action == 2:
        print(user.get_balance())
    elif action == 3:
        print(user.import_income())
    elif action == 4:
        print(user.import_expenses())
    action = get_int("1 Transaction  2 Balance  3 Import income  4 Import expenses  0 Done\n> ")

history = get_int(
    "1 Income history  2 Expense history  3 All transactions  "
    "4 Expenses by category  5 Income by category\n> "
)
if history == 1:
    print(user.get_income())
elif history == 2:
    print(user.get_expenses())
elif history == 3:
    print(user.get_transactions())
elif history == 4:
    print(user.get_expenses_by_category())
elif history == 5:
    print(user.get_income_by_category())
else:
    print("Invalid.")

export = get_int("1 Export expenses  2 Export income  3 Plot expenses  4 Plot income\n> ")
if export == 1:
    user.export_expenses()
elif export == 2:
    user.export_income()
elif export == 3:
    user.plot_expenses()
elif export == 4:
    user.plot_income()
else:
    print("Invalid.")
