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

def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("You must enter a number!")

def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("You must enter a number!")

userName=input("Please give as your name: ")
account_deposit = get_float_input("Please give as your money Account")
user=User(userName,account_deposit)
energy=get_int_input("Please Select Energy : Press 1 for Transaction. 2 For showing balance!")
while energy in [1,2] :
    if energy ==2:
        print(user.get_balance())
    elif energy ==1:
        payment=create_transaction()
        transaction_mode=get_int_input("Please select: Press 1 to add money to your account . 2 To define an expense")
        if transaction_mode==1:
            print(user.add_money(payment))
        elif transaction_mode==2:
            print(user.spend_money(payment))
        else:
            print("Invalid Transaction")
    else:
        print("Invalid")
    energy=get_int_input("Please Select Energy : Press 1 for Transaction. 2 For showing balance!")
print("If you want to see the history:")
print("1. History of Incomes")
print("2. History of Expenses")
print("3. History of All transactions")
history_transactions=get_int_input("Select: ")
if history_transactions==1:
    print(user.get_income())
elif history_transactions==2:
    print(user.get_expenses())
elif history_transactions==3:
    print(user.get_transactions())
else:
    print("Invalid")
exports=get_int_input("Would you like to have something as an export?")
if exports==1 :
    user.export_expenses_as_json()
elif exports== 2:
    user.export_incomes_as_json()
else:
    print("Invalid")

    

