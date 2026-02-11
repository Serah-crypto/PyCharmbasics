
#Task 1:create the class

#create a class called student
#attributes:fullname,course,age,feespaid


#Task2:create multiple objects
#create at least 3 student objects from the same class with different values and display the same info.


class Student :
     def __init__(self,Fullname,course,age,feespaid) :
         self.fullname = Fullname
         self.course = course
         self.age = age
         self.feespaid = feespaid


std1 = Student("Jefferson Kamau","Computer Science",30,True)
print("First Student:")
print(std1.fullname),print(std1.course),print(std1.age),print(std1.feespaid)
print()

std2 = Student("Favour Mwangi","MIT",23,False)
print("Second Student:")
print(std2.fullname),print(std2.course),print(std2.age),print(std2.feespaid)
print()

std3 = Student("Vitalis Okemo","Analytical Chemistry",19,False)
print("Third Student:")
print(std3.fullname),print(std3.course),print(std3.age),print(std3.feespaid)
print()

std4 = Student("Nelius Nkirote","Law",20,True)
print("Fourth Student:")
print(std4.fullname),print(std4.course),print(std4.age),print(std4.feespaid)
print()

std5 = Student("Abigael Njihia","Software engineering",36,True)
print("Fifth Student:")
print(std5.fullname),print(std5.course),print(std5.age),print(std5.feespaid)
print()


