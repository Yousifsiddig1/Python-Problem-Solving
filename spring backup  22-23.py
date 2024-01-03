spring backup  22-23:

# list four lists methods and descripe
#max : returns the highest number in a list 
# min : returns the lowest number in a list 
# pop(index) : returns the element and removes it from the list 
# sort : sort the list from the largest element to the lowset
# append(item): add the item at the end of the list
#########################################################
#Write a python program that consists of the main function and a recursive function print_num that accepts a positive integer argument, n, and prints every second number from n down to a minimum of 0. The main function should include the following:
#Prompt the user to enter a  non-negative number
#Validates the input. If not positive, the user should keep  re-entering the integer until a correct value is entered.
#Calls the recursive function print_num
def main():

    while True:
        n = int(input("Enter a positive starting number"))
        if n > 0 :
            print_num(n)
            break
        else:
            n=int(input("Wrong  entry ! , Enter  positvie starting number :"))
            print_num(n)
            break
def print_num(n):
    if n >=0:
        print(n,end=' ')
        print_num(n-2)
#main()
# requested to write a python program that does the following:
#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a Perimeter() method to calculate the perimeter of the rectangle 
#Create an Area() method to calculate the area of ​​the rectangle.
#Create a method display() that display the length, width, perimeter, and area of an object created using an instantiation on rectangle class.
#N.B: Perimeter= 2*(length + width), Area= (length * width)

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width=width
    def Area(self):
        area = self.length*self.width 
        return area
    def Perimeter(self):
        perimeter= 2*(self.length+self.width)
        return perimeter
    def display(self):
        print(f"the width is : {self.width} \n the length is : {self.length} \n the Area is : {self.Area()}")
        print(f'the perimeter is :{self.Perimeter()}')
x=Rectangle(2,3)
x.display()

