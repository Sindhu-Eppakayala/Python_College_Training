# Day03_typecasting_problems

#Q.write a python program to print upper case and lower case letters?
a=int(input("enter a starting range of capital letters:"))
b=int(input("enter a ending range of capital letters:"))
c=int(input("enter a starting range of small letters:"))
d=int(input("enter a ending range of small letters:"))
print("CAPITAL LETTERS:")
for i in range(a,b):
    print(chr(i),end=" ")
print("\nSMALL LETTERS:")
for i in range(c,d):
    print(chr(i),end=" ")



#Q.write a python program to print upper case and lower case letters in single code?
a=int(input("enter a numnber:"))
for i in range(65,91): #--->O(26) ---O(n)
    print(chr(i),end=" ")
print("\n")
for j in range(97,123): #--->O(26) ---O(n)
    print(chr(j),end=" ")



#Q.write a python program to print alphabets with time complexity O(1)?
a=("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
b=("a b c d e f g h i j k l m n o p q r s t u v w x y z")
print(a,b)

for i in range(65,66): -----O(1)
    print(chr(i),end=" ")
print("/n")
for i in range(97,98): -----O(1)
    print(chr(i),end=" ")

T.C=O(1)+O(1)=O(1)



#Q. write a python code to check a given character is a vowel or not?
a=input("enter a letter : ")
for i in a:
    if i in 'a,e,i,o,u,A,E,I,O,U':
        print(i,'=vowel')
    else:
        print(i,"=consonent")

T.C=O(1)


#Q. write a python code to check a given character is a vowel or not?
a=input("enter a word : ")
for i in a:
    if i in 'a,e,i,o,u,A,E,I,O,U':
        print(i,'=vowel')
    else:
        print(i,"=consonent")

T.C=O(n)


#Q.write a program to check a given value is a alphabet or a nummber or special character?
#CODE-1:
a=input("enter a value:")
for i in a:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        print(a, "=ALPHABETS")
        if i in 'a,e,i,o,u,A,E,I,O,U':
            print(i,'=vowel')
        else:
            print(i,"=consonent")
    elif i in '0 1 2 3 4 5 6 7 8 9':
        print(a ,"=NUMBER")
    else:
        print(a,"=SPECIAL CHARACTER")

T.C=O(n)
O(space)=O(1)


CODE-2:
a=input("enter :")
if a.isalpha():
    if a in 'a,e,i,o,u,A,E,I,O,U':
      print(a,"is a vowel")
elif a.isdigit():
   print("number")
else:
    print("special characters")

T.C=O(1)
O(space)=O(1)





#Q.write a python program for counting the digits
#test data: enter the number 1234
#expected output: 4
#code-1:
a=input("enter a number")
count=0
for i in a:
    count=count+1
print(count)

T.C=O(1)

#code-2:
a=input("enter a number:")
print(len(a))

T.C=o(1)

#code-3:
num=input("enter a number:")
count=0
for i in range(len(num)):
    count+=1
print(count)

T.C=o(1)-->in 1st iteration it finds len(number), it iterates 4 times then T.C=O(n)
then T.C in best case = O(1), worst case= O(n)



#COMPANY MOST ASKED QUESTIONS


#Q.PROBLEM STATEMENT: Restaurant bill splitter
#you and your friend went to a restaurant and want to split the bill equally
#give the total bill amount and the number of people, write a program to calculate how much each person should pay.
#if the number of people is 0,print"INVALID INPUT".
#Input format
#first line: integer bill amount
#second line: integer people
#constraints
#0<=bill_amount<=10^6
#0<=people <=100

#OUTPUT FORMATE
#print the amount each person has to pay.
#if people=0 ->print: INVALID INPUT

#test data:
#cost:1000
#people:4
#target=250

#CODE-1:
bill_amount=int(input("enter a number:"))
people=int(input("enter number of people:"))
if bill_amount>0 and bill_amount<=1000000:
    if people>0 and people<=100:
        total_amount=bill_amount//people
        print("bill per person:",total_amount)
else:
    print("INVALID INPUT")

#CODE-2:
cost=int(input("enter amount"))
people=int(input("enter no of people"))

if 0<=cost<=1000000 and 0<=people<=100:
  target=cost//people
  print(target)
else:
    print("invalid input")




#PROBLEM STATEMENT: Bus Ticket price calculation
#Q.a bus ticket price depends on the paddengers age.
#if thhe age below 12 -->half ticket (50% of price)
#if age is 60 or above --> 30%discount
#otherwise -->full ticket price
#write a program that takes the ticket price and age as input and prints the final amount to be paid
#input formate:
#first line: integer price
#second line: integer age

#OUTPUT FORMATE:
#print the final ticket price after applying the discount
#TEST CASE:
#100
#10

price=int(input("enter price of ticket:"))
age=int(input("enter age of the person:"))
if age<=12:
    discount=(price*50)/100
    final_price=price-discount
elif age>=60:
    discount=(price*30)/100
    final_price=price-discount
else:
    final_price=price
print("final ticket price = ",final_price)




#PROBLEM STATEMENT: Shopping Bill Generator
#A customer purchases 5 items from a shop.
#the shop charges 18% GST on the total purchase amount.
#write a program that takes the price of 5 iteams as input and prints:
#total cost of items
#GST amount
#final payable amount(including GST)
#INPUT FORMAT:
#five lines of inputs, each containing the price of an item.

#OUTPUT FORMATE:
#print three values;
#total:total price of items
#GST:GST amount(18% of total)
#final amount: total+GST

#CODE-1:
cost = 0
for i in range(1,6):
    purchase_items=int(input("item:"))
    cost= cost + purchase_items
print("Total:",cost)

GST= cost * 18/100
print("GST:",GST)
final_amount=cost+GST
print(final_amount)

#CODE-2:
i1=int(input("enter amount of i1:"))
i2=int(input("enter amount of i2:"))
i3=int(input("enter amount of i3:"))
i4=int(input("enter amount of i4:"))
i5=int(input("enter amount of i5:"))
total=i1+i2+i3+i4+i5
GST=total*0.18
final_amount=total+GST
print("total:",total)
print("GST:",GST)
print("Final amount:",final_amount)



#PROBLEM STATEMENT: Mobile recharge offer system:
# A mobile network comapany provides cashback offers based on the recharge amount.
#recharge below rs100-->no offer
#recharge rs100 - rs 299-->cashback rs10
#recharge rs300 - rs 499 -->cashback rs25
#recharge rs 500 or more -->cashback rs50

# WAP that takes the recharge amount as input and prints the cashback amount.

# INPUT FORMAT:
# A single integer amount representing the recharge value.


#OUTPUT FORMAT
#print the cashback amount.
#if no offer applies,print: NO CASHBACK

#constraints: 0<=amount<=10000

recharge_amount=int(input("enter recharge amount:"))
if recharge_amount>=0 and recharge_amount<=10000:
    if recharge_amount<=100:
        print("NO OFFER")
        print("NO CASHBACK")
        print("final recharge amount=",recharge_amount)
    elif recharge_amount>=100 and recharge_amount<=299:
        print("CASHBACK=10rs")
        print("final recharge ammount=",recharge_amount-10)
    elif recharge_amount>=300 and recharge_amount<=499:
        print("CASHBACK=25rs")
        print("final recharge amount=",recharge_amount-25)
    elif recharge_amount>=500:
        print("CASHBACK=50")
        print("final recharge amount=",recharge_amount-50)
    else:
        print("INVALID AMOUNT")




#Q.write a python program to find a given element is present or not?
#TEST DATA:
#enter the elements:1 3 5 7 9
#enter the target:5
#OUTPUT:
#element present :2


element=input("enter the elements:")
target=int(input("enter the target:"))
a=list(element)
print(a)
for i in range(elemets,5):
    if element==target:
        print("element present:",i)


a=[]
target=int(input("enter target numner:"))
for i in range(target):
    elements=int(input("enter elements:"))
    a.append(elements)
print(a)
for i in a:
    if target==i:
        print("element present:",i)
