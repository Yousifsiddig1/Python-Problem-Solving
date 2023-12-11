# final spring 22-23
# part 2 
# Question 4 
def find_quotiant_and_remainder(a,b):
    quotient = a // b
    remainder = a % b
    return  quotient, remainder 
a = int(input("Enter a :"))
b = int(input("Enter b :"))
quotiant , remainder =find_quotiant_and_remainder(a,b)
print('Quotiant', quotiant)
print('Remainder',remainder)
# part 3 
# Question 1 
my_list = [14,12,9,11,19]
filename = input("Enter file name :")
  #open the file
file = open(filename, 'w') # or with open(filename, 'w') as file: 
for i in my_list:
    file.write(str(i) + '\n')
file.close() # if u used ' with open(filename, 'w') as file:' you dont need to close 
# Question 2 
def print_odds(number):
    for i in range(number,0,-1):
        if i%2 !=0:
            print(i,end=' ')
def main():
    number = int(input("Enter a positive Starting number")) # prompt the user to enter a positive starting nubmer 
    while True:
        if number <= 0 :
            number= int(input("Wrong entry ! Enter a positive starting number "))
        else:
            print_odds(number)
            break
main()

# Question 3
# Will add soon 

#Question 4
class student:
    def __init__(self,name,age,grades):
        self.name = name 
        self.age= age 
        self.grades = grades
    def average(self):
        total = sum(self.grades)
        average =total/len(self.grades)
        return  average
    def display(self):
        print('Name:',self.name)
        print('Age',self.age)
        print('Grades:',self.grades)
        print('Average is ',self.average())
student1=student('Ali',20,[70,80,90])
student1.display()
