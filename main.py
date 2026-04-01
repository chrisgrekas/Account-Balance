from tracker import User
from tracker import Transaction
from datetime import datetime

def create_transaction():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    while True:
        try:
            amount = float(input("Please give me amount of money:"))
            break
        except ValueError:
            print("Please give as a number")
    category = input("Please specify the category:")
    return Transaction(amount, category, now)

userName=input("Please give as your name: ")
while True:
    try:
        account_deposit = float(input("Account Deposit: "))
        break
    except ValueError:
        print('You must enter a number')

user=User(userName,account_deposit)
while True:
    try:
        energy = int(input("Please Select Energy : Press 1 for Transaction. 2 For showing balance!"))
        break
    except ValueError:
        print("You must choose a number.Press 1 for Transaction. 2 For showing balance!")
while energy in [1,2] :
    if energy ==2:
        print(user.get_balance())
    elif energy ==1:
        payment=create_transaction()
        while True:
            try:
                transaction_mode=int(input("Please select: Press 1 to add money to your account . 2 To define an expense"))
                break
            except ValueError:
                print("You must pick a number")

        if transaction_mode==1:
            print(user.add_money(payment))
        elif transaction_mode==2:
            print(user.spend_money(payment))
        else:
            print("Invalid Transaction")
    else:
        print("Invalid")
    while True:
        try:
            energy = int(input("Please Select Energy : Press 1 for Transaction. 2 For showing balance!"))
            break
        except ValueError:
            print("You must choose a number.Press 1 for Transaction. 2 For showing balance!")
print("If you want to see the history:")
print("1. History of Incomes")
print("2. History of Expenses")
print("3. History of All transactions")
while True:
    try:
        history_transactions = int(input("Select: "))
        break
    except ValueError:
        print("Please choose a number")
if history_transactions==1:
    print(user.get_income())
elif history_transactions==2:
    print(user.get_expenses())
elif history_transactions==3:
    print(user.get_transactions())
else:
    print("Invalid")

    

