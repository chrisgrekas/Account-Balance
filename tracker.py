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
    
    
        


class Transaction:
    def __init__(self,amount,category,date):
        self.amount=amount
        self.category=category
        self.date=date
    def __repr__(self):
        return f'Amount of transaction : {self.amount} , Category : {self.category} , at :{self.date}'
    
    