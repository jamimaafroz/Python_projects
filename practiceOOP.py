#practice question: 
#create account class with 2 attributes - balance and Account no.
#Create methods for debit , credit & printing the balance

class Account ():
    def __init__(self,account_no ,balance):
        self.account_no = account_no
        self.balance = balance
    
    def debit(self,amount):
        self.balance-= amount
        print("TK" , amount , "was credited")
    
    def credit(self , amount):
        self.balance += amount
        print("Rs",amount ,"was credited")

Account1 = Account(12, 1000000) 
Account1.debit(5000)
Account1.credit(100)
print(Account1.account_no ,Account1.balance )

