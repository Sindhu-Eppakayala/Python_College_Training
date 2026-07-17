#  Day06_oop_constructors_examples

###RECURSION
#Fibinoic series:
def fibo(nums):
    if nums<=1:
        return nums
    return fibo(nums-1)+fibo(nums-2)
print(fibo(5))


#Factorial of a number:
def fact(num):
    if num==1:
        return num
    return num*fact(num-1)
print(fact(3))



##OBJECT ORIENTED PROGRAMMING

## check notes for problems

#Q.PROBLEM STATEMENT:
#create a student class with: name, roll number, marks
#methods:display(),calculate_percentage()
class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
    def calculate_percentage(self):
        percentage=self.marks/100*100
        print(percentage)
    
c=student("sindhu", 37,95)
c.display()
c.calculate_percentage()
        



#PROBLEM STATEMENT:
#Q.create a bank account
#Methods: deposit(),withdraw(),check_balance()
class bank:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        if amount<=0:
            print("INVALID AMOUNT:")
        else:
            self.balance+=amount
            print("deposit is successfull")
    def withdraw(self,amount):
        if amount<=0:
            print("INVALID AMOUNT")
        elif amount > self.balance:
            print("INSUFFICIENT AMOUNT")
        else:
            self.balance-=amount
            print("Withdrawal successful")
    def check_balance(self):
        print(self.balance)
b=bank()
b.deposit(500)
b.check_balance()
b.withdraw(1000)
b.check_balance()
b.check_balance()





#Q.PROBLEM STAEMENT:Rectangle class
#create a rectangle class with: length,width
#methods: area()(L*W),perimeter()(2*(L+B))
class Rectangle_class:
    def __init__(self,length,width):
        self.width=width
        self.length=length
    def area(self):
        print("area:",self.length*self.width)
    def perimeter(self):
        print("perimeter:",2*(self.width+self.length))
b=Rectangle_class(10,20)
print(b.length)
print(b.width)
b.area()
b.perimeter()



##LIST:
#Q.square the list of elements?
n=[1,2,3,4,5]
for i in range(n):
    print(i**2,end=" ")
    





##INHERITANCE:
#single inheritance:
#defination:single inheritance where you will have one base class and one derive class or one child class or one parent class
#it is used to aquare properties from parent class to child class or base class to derived class

#Example:
class base:
    def __init__(self):
        print("Iam a base class")
    def book(self,pageno):
        print("book")
class derived:
    def __init__(self):
        super().__init__()#used to call constructor
        print("Iam derived class")
    def chair(self,count):
        print("chair")
c=base()
pencil=base()
pencil.book(10)
d=derived()
d.chair(100)


##MULTIPLE INHEREITANCE:
#DEFINATION:
#Multiple inheritance it is a inheritance in which has 2 or more base class and only 1 derived class
#in derived class priority matters from left to right
#Eample:
class A:
    def __init__(self):
        print("Iam  A")
    def a(self):
        print("Iam a")
class B:
    def __init__(self):
        super().__init__()
        print("Iam B")
    def b(self):
        print("Iam b")
class c(B,A):
    def __init__(self):
        super().__init__()
        print("Iam C")
    def c(self):
        print("Iam c")

pen=c()
pen.a()
pen.b()
pen.c()


#ENCAPSULATION:
#eg: PUBLIC METHOD
class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def display(self):
        print(self.balance)
b=BankAccount()
b.deposit(2000)
b.withdraw(500)
b.display()
print(b.balance)



#eg: PRIVATE METHOD (For security reasons)
class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def get_amount(self):
        print(self.__balance)
        #pass ##used to skip the function (same as break)
    def set_amount(self,amount):
        self.__balance+=amount
        print(self.__balance)
        #pass ##used to skip the function (same as break)

b=BankAccount()
b.deposit(2000)
b.withdraw(500)
b.get_amount()
b.set_amount(15000)
#(b.__balance)
