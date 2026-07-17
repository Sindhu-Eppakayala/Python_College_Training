#Day-01 -Basic Programs

#operators:
#Arthematic operations:
#adding of 2 numbers:
a=10
b=20
print("Adding of 2 numbers:",a+b)
print("subtracting of 2 numbners:",a-b)
print("multiplying of 2 numbers:",a*b)
print("dividing of 2 numbers:",a/b)
print("module of 2 numbers:",a%b)
print("exponential of 2 numbers",a**b)
print("division of 2 numbers in float",a//b)


#Swap of 2 numbers:
a=10
b=20
t=a
a=b
b=t
print("After swapping:",a,b)

#Assignment operator:
a=10
b=20
a=b
print("the value of a=",a)

a=10
b=20
a+=b
print("the value of a=",a)

a=10
b=20
a-=b
print("the value of a=",a)

a=10
b=20
a/=b
print("the value of a=",a)

a=10
b=20
a//=b
print("the value of a=",a)

a=10
b=20
a*=b
print("the value of a=",a)

a=10
b=20
a**=b
print("the value of a=",a)

a=10
b=20
a%=b
print("the value of a=",a)



#Comparision operator:
a=10
b=20
print("is a equal to b",a==b)
print("is a not equal to b",a!=b)
print("is a greater than to b",a>b)
print("is a less than to b",a<b)
print("is a greater than equal to b",a>=b)
print("is a less than equal to b",a<=b)


#Indentation:
a=10
b=10
if a==b:
    print("yes a is equal to b")
print("out of if block")

a=10
b=20
if a==b:
    print("yes a is equal to b")
print("out of if block")


#programs:
#Q. write a program to take a input runtime?
a=int(input("enter a:"))
b=int(input("enter b:"))
print("value of a+b:",a+b)


#Q. write a program to check a person is eligible to vote or not?
age=int(input("Enter your age:"))
if age>=18:
    print("your eligilble to vote")
else:
    print("your not eligible to vote")


#Q. write a program to print the given number is even or odd?
num=int(input("enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")


#Q. write a program to accept the speed of the car. If the car speed is greater than or equal to 80. then print the message 'slow Down your car'.?
speed=int(input("enter your speed of the car:"))
if speed>=80:
    print("Slow Down Your Car")


#Q. write a program to that accepts the percentage of a student. After receiving the percentage the program should check whether the percentage is grater than or equal to 40. if it is then he program should print "PASS"?
per=int(input("enter your percentage:"))
if per>=40:
    print("PASS")
else:
    print("FAIL")


#Q. write a program to accept the age of a person. program should print the message as per following conditions
#if the age is greater than 18, you can ride a bike
#if age is less than 18, you cant ride a bike
#if age is exactly 18, you can ride a bike with the lesson holder

age=int(input("enter age:"))
if age>18:
    print("YOU CAN RIDE THE BIKE")
elif age<18:
    print("YOU CAN'T RIDE A BIKE")
elif age==18:
    print("YOU CAN RIDE A BIKE WITH THE LESSON HOLDER")



#Q. write a program to accept the three angles of a triangle.
#if the sum if a angle is 180, print 'triangle is possible'
#if the sum of the angles is not equal to 180, print 'Triangle is not possible'
a=int(input("enter angle 1:"))
b=int(input("enter angle 2:"))
c=int(input("enter angle 3:"))
sum=a+b+c
if sum==180:
    print("TRIANGLE IS POSSIBLE")
elif sum!=180:
    print("TRIANGLE IS NOT POSSIBLE")



#Q. write a program to ask the user whether it is raining.
# the user will reply with' Y' for Yes or 'N' for No.
# if the user enters 'Y' print 'Bring an umbrella with you'
# if the user enters 'N' print 'No need for an umbrella'
a=input("enter Y/N: ")
if a=='Y':
    print("BRING AN UMBRELLA WITH YOU")
elif a=='N':
    print("No NEED FOR AN UMBRELLA")



#Q.write a program to accept the current kilometer reading of your ccar and the kilometer reading at the last service.
# then, calculate the difference between these two readings,{difference=currentkm-lastservicekm}
#if the differenece is greater than or equal to 10000, it prints" please service your car"
#if the difference is less than 10000, print" No servicing required this time"
currentKM=int(input("enter your current kilometer readings:"))
lastserviceKM=int(input("enter your last service readings:"))
difference=currentKM-lastserviceKM
if difference>=10000:
    print("PLEASE SERVICE YOUR CAR")
else:
    print("NO SERVICING REQUIRED AT THIS TIME")



#q. write a program to accept marks for three subjects and calculate the obtained marks and percentage of a student.
#if the percentage is greater than or equal to 40, print "pass"
#if percentage is less than 40, print "fail"
#(NOTE: obtained marks =m1+m2+m3, percentage=(obtained marks/300)*100)
m1=int(input("enter 1st subject marks:"))
m2=int(input("enter 2nd subject marks:"))
m3=int(input("enter 3rd subject marks:"))
sum=m1+m2+m3
percentage=(sum/300)*100
if percentage>=40:
    print("PASS")
elif percentage<40:
    print("FAIL")



#Q. write a program to accept 3 products price and calculate the total price.
#if the total is less than 500 then give 10% discount of total price
#if the total is greater tham or equal to 500 then give 30% discount of total price and print total price,how much discount,discount amount and final price after discount
p1=int(input("enter product1 price:"))
p2=int(input("enter product2 price:"))
p3=int(input("enter product3 price:"))
total=p1+p2+p3
print(total)
if total>=500:
    print("You Got 30% discount")
    discount=(total*30)/100
    print("discount amount",discount)
    final_price=total-discount
    print("Final price after discount:",final_price)
if total<500:
    print("You Got 30% discount")
    discount=(total*10)/100
    print("discount amount",discount)
    final_price=total-discount
    print("Final price after discount:",final_price)    


#Q.a company decided to give bouns of 10% to employees.accept the year of service of an employee.
    #if his/her year of service is more than or equal to 5years, then print "10% bonus approved"
    #if his/her year of service is less than 5years, then print"No bonus approved.

#Q.write a program to calculate the basic salary of an employee and calculate the gross salary based on the following conditions:
#if the basic salary is less than or equal to 10000, then the HRA(house rent allowance) is 40% and DA(Dearness Allowance) is 9%.
#if the basic salary is greater than 10000, then the HRAis 30% and DA is 11%
#NOTE:gross salary=basic salary+HRA+DA
salary=int(input("enter the basic salary:"))
if salary<=10000:
    HRA=(salary*40)/100
    DA=(salary*9)/100
    gross_salary=salary+HRA+DA
    print("HRA,DA,GROSS_SALAR",HRA,DA,gross_salary)
if salary>10000:
    HRA=(salary*30)/100
    DA=(salary*11)/100
    gross_salary=salary+HRA+DA
    print("HRA,DA,GROSS_SALAR",HRA,DA,gross_salary)



#Q.write a program to find out no of currencies will present?
#input:11
#output:2000rs=9,500rs=1,100rs=1,50rs=1,20rs=1,10rs=1,5rs=1,2rs=1,1rs=1,total=18
amount=int(input("enter your amount:"))
count=0
if amount>=2000:
    rs2000=amount//2000
    count=count+rs2000
    print("2000rs notes:",rs2000)
    amount=amount%2000
if amount>=500:
    rs500=amount//500
    count=count+rs500
    print("500rs notes:",rs500)
    amount=amount%500
if amount>=200:
    rs200=amount//200
    count=count+rs200
    print("200rs notes:",rs200)
    amount=amount%200
if amount>=100:
    rs100=amount//100
    count=count+rs100
    print("100rs notes:",rs100)
    amount=amount%100
if amount>=50:
    rs50=amount//50
    count=count+rs50
    print("50rs notes:",rs50)
    amount=amount%50
if amount>=20:
    rs20=amount//20
    count=count+rs20
    print("20rs notes:",rs20)
    amount=amount%20
if amount>=10:
    rs10=amount//10
    count=count+rs10
    print("10rs notes:",rs10)
    amount=amount%10
if amount>=5:
    rs5=amount//5
    count=count+rs5
    print("5rs notes:",rs5)
    amount=amount%5
if amount>=2:
    rs2=amount//2
    count=count+rs2
    print("2rs notes:",rs2)
    amount=amount%2
if amount>=1:
    rs1=amount//1
    count=count+rs1
    print("1rs notes:",rs1)
    amount=amount%1
print(count)



#Q.write a program for electricity bill
#1to 100 units rs 6
#101 to 200 units RS 8
#201 to 300 units RS 10
#301 to 400 units RS 12
#more than 400 units RS 14.5_5
units=int(input("enter number of units:"))
amount=0
if units>=1 and units<=100:
    amount=units*6
elif units>=101 and units<=200:
    amount=100*6+(units-100)*8
elif units>=201 and units<=300:
    amount=100*6+100*8+(units-200)*10
elif units>=301 and units<=400:
    amount=100*6+100*8+100*10+(units-300)*12
elif units>400:
    amount=100*6+100*8+100*10+100*12+(units-400)*14.5
print(amount)

#RANGE:

#write a program to print 1 to 10 numbers
for i in range(1,20,2):
    print(i)

    
#write a program to print your name 10 times:
for i in range(10):
    print("SINDHU")

for i in range(10):
    print("SINDHU",i)

for i in range(10):
    print("SINDHU",i+1)



#write a program to print even numbers from 1 to 20?
for i in range(1,20):
    if i%2==0:
        print(i)

        #(OR)
for i in range(0,20,2):
    print(i)

for i in range(2,20+1,2):
    print(i,end=' ')

#Q.write a program to print the numbers which are divisible by 2 and  3 from 1 to 50?
for i in range(1,50):
    if i%6==0:
        print(i,end=' ')


#Q.write a program to print multiplication table of a given number?
n=int(input("enter a number:"))
for i in range(1,11):
    print(n,'X',i,"=",n*i)


#Q.print sum of n natural number?
count=0
for i in range(11):
    count=count+i
print("sum of N:",count)



#Q.find the factorial of a given number?
n=int(input("enter the number:"))
fact=n*10


#Q.write a program to print telugu letters?
for i in range(3077,3134):
    print(chr(i),end=' ')


#Q.write a program to print ascii characters with value eg: A:65?
for i in range(65,91):
    print(chr(i),':', i)

for i in range(256):
    print(chr(i),':', i)



#Q.for loop with sequence type
List1=[10,20,20.5]
for i in List1:
    print(i)


str="SINDHU"
for i in str:
    print(i)
