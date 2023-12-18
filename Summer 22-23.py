# Summer 2022 / 2023 
 # M110
# Part 1 MCQ 
# Q-1 ) b    #incorrect because tuples are not enclosed with curly brackets 
# Q-2 ) c) 3
# Q-3 ) a)    #it is the easist way because the python folder is located under the same folder 
# Q-4 ) c) Widget  
# Q-5 ) c) Bye! 
 #Q-6 ) B) 0 1 2  # when x = 3 get out of(breaks) the loop 
# Q-7 ) D) 
# Q-8 ) B)
# Q-9 ) D)
# Q-10) D)

# PART 3 :
#Q-1
my_tuple = ('A',18,16,'B',12,8,'C',10,7)
list1 = list(my_tuple)
list2= []
for i in range(0,len(list1)-1,3):
    list2.append(list1[i])
    list2.append((list1[i+1]+list1[i+2]) / 2)

print(list2)
  
#Q-2 
x =[[12,7,3],[4,5,6],[7,8,9]]
y = [ [5,8,1],[6,7,3],[4,5,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        result[i][j] = x[i][j]+y[i][j]
for i in result:
    print(i)
#Q-3
class Computation():
    def __init__(self,n):
        self.n = n 
    def factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    def Sum(self,n):
        mySum=0
        for i in(1,n+1):
            mySum += i 
        return mySum
n = int(input("Enter n :"))
x=Computation(n)
print(" The Factorial is : ",x.factorial(n))
print(f"The sum is : {x.Sum(n)}")

#Q-4
from tkinter import *  #A
class MyGUI :# B
    def __init__(self):
        self.root =Tk() #C
        self.root.title("M110 SU23")
        self.label1=Label(self.root,text=' Final Exam')
        self.label2=Label(self.root,text='Good Luck!') #D
        self.label1.pack(side='left') #E
        self.label2.pack(side='right')
        mainloop() # F
my_gui =MyGUI()
