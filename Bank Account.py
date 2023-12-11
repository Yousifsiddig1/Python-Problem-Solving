 # Basic Bank Account class 
class BankAccount:
    def __init__(self,name,sex,AccNumber,balance = 0):
        self.name = name
        self.sex = sex
        self.AccNumber= AccNumber
        self.balance = balance
    def deposit(self,amount): # create a method to deposit
        if  amount > 0:
            self.balance += amount
            return self.balance
    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount 
            self.balance = self.balance - amount / 10 # to take tax from the balance
            return self.balance
    def display(self):
        print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {self.balance}')
while True:
    # ask the user about what he want to do 
    depOrWith = input(" d to deposit or w to withdraw or dis to display Account info :").lower() 
    if depOrWith == 'd': # d means that the user want to deposit 
        amount = int(input("Enter the amount to deposit:")) # ask the user how much to deposit
        break
    elif depOrWith == 'w': # w means that the user want to withdraw
        amount = int(input("Enter the amount to withdraw:"))
        break
    elif depOrWith == 'dis': # to display info 
        break
    else:
        print("Invalid input , Try again ")
person1 =BankAccount('Yousif ','Male ','1234-8439-3242-1234', 100)
if depOrWith == 'w':
    person1.withdraw(amount)
    person1.display()

elif depOrWith =='d':
    person1.deposit(amount)
    person1.display()
else:
    person1.display()
