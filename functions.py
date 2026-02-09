#Functions/methods - block of codes used to perform a task


# 1.Standard library functions/ Inbuilt - already exists
y = max(56, 67, 35, 6788, 9802)
print(y)

x = min(298, 340, 457, 100,2387,1,109)
print(x)


# 2.User defined functions

def school():
    print("eMobilis")

school() #calling a function


def multiply():
    print (15*5)
multiply()

#Parameters/Variables
def multiply(x,y):
    print(x * y)

#Arguements/values
multiply(15,6)
multiply(15,56)



#python program to display details of 5 employees at emobilis
#use a user defined function with help of parameters and arguments

# details - full name, position, age, gender



print()

def employees(fullname , position, age, gender):
     print(fullname)

     print(position)

     print(age)

     print(gender)


employees("Lentine Khakai", "Cyber security instructor", 30, "Female")
print()
employees("Nelson Oginga", "ICT Manager",28,"male")
print()
employees("Ken Gikunda", "managing director",35,"male")
print()
employees("Kimanzi Mwendwa", "Centre Manager", 42, "Male")
print()
employees("Peter Gachuki", "Lecturer", 37, "Male")
print()






