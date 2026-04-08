import json
import matplotlib.pyplot as plt
import numpy as np
class User:
    def __init__(self,name,account_deposit):
        self.name=name
        self.account_deposit=account_deposit
        self.transactions=[]
        self.expenses=[]
        self.income=[]
    def __repr__(self):
        return f'Hello {self.name}'

    def add_money(self,transaction):
        self.account_deposit+=transaction.amount
        self.transactions.append(transaction)
        self.income.append(transaction)
        return f'{transaction.amount} of money has been added to your account.The reason is {transaction.category} and the date is {transaction.date}. You now have {self.account_deposit} into your account'
    def spend_money(self,transaction):
        if transaction.amount> self.account_deposit:
            return f"Your account does not have so much money!"
        else:
            self.account_deposit-=transaction.amount
            self.transactions.append(transaction)
            self.expenses.append(transaction)
            return f'{transaction.amount} of money has been withdraw to your account.The reason is {transaction.category} and the date is {transaction.date}. You now have {self.account_deposit} into your account'
    def get_balance(self):
        return f"Hello {self.name} you now have {self.account_deposit}"
    def get_transactions(self):
        return self.transactions
    def get_income(self):
        return self.income
    def get_expenses(self):
        return self.expenses
    def export_expenses_as_json(self):
        data=[]
        for t in self.expenses:
            data.append({"amount": t.amount, "category": t.category, "date": t.date})
        with open("expenses.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Έτοιμο! Το αρχείο expenses.json δημιουργήθηκε.")

    def export_incomes_as_json(self):
        data=[]
        for t in self.income:
            data.append({"amount": t.amount, "category": t.category, "date": t.date})
        with open("incomes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Έτοιμο! Το αρχείο incomes.json δημιουργήθηκε.")

    def import_incomes_from_json(self):
        with open("incomes.json","r") as file:
            data=json.load(file)
        for item in data:
            t = Transaction(item["amount"], item["category"], item["date"])
            self.income.append(t)
            self.account_deposit += t.amount
        return(f"Your new account deposit are : {self.account_deposit}")

    def import_expenses_from_json(self):
        with open("expenses.json","r") as file:
            data=json.load(file)
        for item in data:
            t=Transaction(item["amount"],item["category"],item["date"])
            self.expenses.append(t)
            self.account_deposit-=t.amount
        return(f"Your new account deposit are : {self.account_deposit}")
    
    def get_expenses_by_category(self):
        expenses_per_category={}
        for expense in self.expenses:
            if expense.category in expenses_per_category:
                expenses_per_category[expense.category] += expense.amount
            else:
                expenses_per_category[expense.category] = expense.amount
        return expenses_per_category    

    def get_income_by_category(self):
        incomes_per_category={}
        for income in self.income:
            if income.category in incomes_per_category:
                incomes_per_category[income.category]+= income.amount
            else:
                incomes_per_category[income.category]=income.amount
        return incomes_per_category

    def get_expenses_as_plot(self):
        expenses_category=self.get_expenses_by_category()
        x=list(expenses_category.keys())
        y=list(expenses_category.values())
        plt.title("Expenses By Category")
        plt.xlabel("Expenses")
        plt.ylabel("Amount")
        plt.bar(x,y)
        plt.show()

    def get_incomes_as_plot(self):
        incomes_category=self.get_income_by_category()
        x=list(incomes_category.keys())
        y=list(incomes_category.values())
        plt.title("Incomes By Category")
        plt.xlabel("Incomes")
        plt.ylabel("Amount")
        plt.bar(x,y)
        plt.show()





    
        


class Transaction:
    def __init__(self,amount,category,date):
        self.amount=amount
        self.category=category
        self.date=date
    def __repr__(self):
        return f'Amount of transaction : {self.amount} , Category : {self.category} , at :{self.date}'
    
    