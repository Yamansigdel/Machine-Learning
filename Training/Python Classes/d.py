
'''
             banking app
personal info       deposit     withdraw
name                balance=    balanc=
balance             balance+    balance-
account no          dep amt     withdraw amt
'''
class bank_account:
    def __init__(self,name,balance,phoneno):
        self.name=name
        self.balance=balance
        self.phoneno=phoneno
    def dash_board(self):
        print("Dashboard")
        print(f"name:{self.name}")
        print(f"balance:{self.balance}")
        print(f"phoneno:{self.phoneno}")
    def withdraw(self,withdraw_amt):
        self.balance=self.balance-withdraw_amt
    def deposit(self,dep_amt):
        self.balance=self.balance+dep_amt
       
bank_id1=bank_account("anup",1000,9841459538)
bank_id2=bank_account("Samek",10000,9841459539)
bank_id1.dash_board()
bank_id1.withdraw(1000)
bank_id1.dash_board()
bank_id1.deposit(1000)
bank_id1.dash_board()