# Day07_inheritance_examples

#multi level inheritance : more than 2 classes
class Apple:
    def mouse(self):
        print("iam mouse")

class Banana(Apple):
    def adapter(self):
        print("iam adapter")

class Cherry(Banana):
    def phone(self):
        print("iam phone")

c = Cherry()
c.phone()
c.adapter()
c.mouse()


#heirarical inheritance
class Apple:
    def mouse(self):
        print("iam mouse")

class Banana(Apple):
    def adapter(self):
        print("iam adapter")

class Cherry(Apple):
    def phone(self):
        print("iam phone")

c = Cherry()
b = Banana()
c.phone()
b.adapter()
c.mouse()
b.mouse()



#Hybrid Inheritance: combination of 2 inheritances
class Apple:
    def mouse(self):
        print("iam mouse")

class Banana(Apple):
    def adapter(self):
        print("iam adapter")

class Cherry():
    def phone(self):
        print("iam phone")

class Bottle(Apple,Cherry):
    def laptop(self):
        print("iam laptop")

b = Banana()
b.adapter()
b.mouse()
    
b1=Bottle()
b1.phone()
b1.laptop()



class apple:
    def rat(self):
        print("IAm a rat")
        
class mango(apple):
    def charger(self):
        print("Iam a charger")
        
class berry():
    def iphone(self):
        print("Iam a Iphone")
        
class water(apple,berry):
    def tab(Self):
        print("Iam a tab")


b=mango()
b.charger()
b.rat()

b1.water()
b1.iphone()
b1.tab()



#METHOD-1:
class Animal:
    def sound(self):
        print("sound")
class dog:
    def sound(self):
        print("bark")
class cat:
    def sound(self):
        print("meow")

a=Animal()
a.sound()
d=dog()
d.sound()
c=cat()
c.sound()


class Animal:
    def sound(self):
        print("sound")
class dog(Animal):
    def sound(self):
        print("bark")
class cat(dog):
    def sound(self):
        print("meow")

c=cat()
c.sound()



class pen:
    def total_sum(self,a=0,b=0,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.total_sum=self.a+self.b+self.c+self.d
p=pen()
p.total_sum(10,20,30,40)
print(p.total_sum)


###problems on patterns:
#write a python code to print the pattern below
#*        *
#**      **
#***    ***
#****  ****
#**********

a=5
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()





#write a python code to print the below patter
#*        *
#**      **
#***    ***
#****  ****
#**********
#****  ****
#***    ***
#**      **
#*        *

a=5
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(1,a):
    for j in range(a-i):
        print("*",end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for i in range(a-i):
        print(("*"),end=" ")
    print()


#just a small design experiment
a=5
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(1,a):
    for j in range(a-i):
        print("*",end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for i in range(a-i):
        print(("*"),end=" ")
    print()
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()




#write a python code to print a diamond with spaces ?
a=5    
for i in range(a-1):
    for j in range(a-i):
        print("*",end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for i in range(a-i):
        print(("*"),end=" ")
    print()
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(a*2-i*2):
        print(" " ,end=" ")
    for j in range(i):
        print("*",end=" ")
    print()




#Q.write a python code to print the given number is amstring or not?
a=int(input("enter a number:"))
temp=a
b=str(a)
n=len((b))

while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10
if sum==num:
   print("Amstrong number")
else:
    print("Not an amstrong number")




##Abstraction:
from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def BMW(self):
        print("BMW")

class bike(car):
    def __init__(self):
        pass

    def BMW(self):
        print("BMW1")
b=bike()
b.BMW()


###
from abc import ABC,abstractmethod
class College(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def details(self,pid,name,marks):
        self.pid=pid
        self.name=name
        self.__marks=marks
    def dispaly(self):
        print(self.pid)
        print(self.name)
        print(self.__marks)
class Student(College):
    def __init__(self):
        pass
    def details(self,pid,name,marks):
        self.pid=pid
        self.name=name
        self.__marks=marks
    def dispaly(self):
        print(self.pid)
        print(self.name)
        print(self.__marks)
class Professor(College):
    def __init__(self):
        pass
    def details(self,pid,name,course):
        self.pid=pid
        self.name=name
        self.course=course
    def display(self):
        print(self.pid)
        print(self.name)
        print(self.course)

s=Student()
p=Professor()
s.details(102,"savika",80)
p.details(220,"navya","python")
s.dispaly()
p.display()
