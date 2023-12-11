فايل الامتحان
https://docs.google.com/document/d/1YNgf6eCGz2tDBto-kHB4H_KqDNPGNBHZ/edit

def num_List(my_list1):
    x= int(input("Enter Positive integer or  negative to stop :"))
    while x >=0:
        my_list1.append(x)
        x= int(input("Enter Positive integer or  negative to stop :"))
    num_list(my_list1)
def num_list(my_list1):
    my_list2=[]
    for  i in my_list1:
        if i %3==0 or i % 7 ==0:
            my_list2.append(i)
    print(my_list2)
my_list1 =[]
num_List(my_list1)
