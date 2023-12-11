# Basic Bank Account class 
class BankAccount:
    def __init__(self,name,sex,AccNumber,balance = 0):
        self.name = name
        self.sex = sex
        self.AccNumber= AccNumber
        self.balance = balance
    def deposit(self,amount):
        if  amount > 0:
            self.balance += amount
            return self.balance
    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
    def display(self):
        print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {self.balance}')

while True:
    depOrWith = input(" d to deposit or w to withdraw:").lower()
    if depOrWith == 'd':
        amount = int(input("Enter the amount to deposit:"))
        break
    elif depOrWith =='w':
        amount = int(input("Enter the amount to withdraw:"))
        break
    else: 
        print("Invalid input , Try again ")
person1 =BankAccount('Yousif ','Male ','1234-8439-3242-1234', 10)
if depOrWith == 'w':
    person1.withdraw(amount)
else:
    person1.deposit(amount)
person1.display()

