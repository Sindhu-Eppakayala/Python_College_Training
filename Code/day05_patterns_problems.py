# Day05_patterns_problems

#Q.ATM withdrawal ask the user for account balance and withdrawal amount.if withdrawal amount>balance -> "insufficient Balance". if amount<= 0 ->"invalid amount". else allow withdrawal
balance=int(input("enter your accounnt balance:"))
withdrawal=int(input("enter your withdrawal amount:"))
if withdrawal > balance:
    print("INSUFFICICENT BALANCE")
elif withdrawal<=0:
    print("INVALID AMOUNT")
else:
    print("ALLOW WITHDRAWAL")



#Q.form a sqaure with stars using conditional statements?
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

#Q.write a code to print the elements in a square formate?
for i in range(5):
    for j in range(5):
        print((i,j),end=" ")
    print()

#Q.form a right angle triangle with 4 stars?
for i in range(5):
    for j in range(5):
        if i==j:
            break
        print("*",end=" ")
    print()
    
#Q.write a python code to print the triangle with 5 stars
#CODE-1:
a=5
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()

#CODE-2:
for i in range(a-1,-1,-1):
    for j in range(a-i):
        print("*",end=" ")
    print()

#Q.form a square  stars where the middle stars need to be removed? 
a=5
b=5
for i in range(a):
    for j in range(b):
        if i==0 or i==a-1 or j==0 or j==b-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



#Q.write a python code to print a right angle triangle?
a=5
for i in range(a-1,-1,-1):
    for j in range(a-i):
        print("*",end=" ")
    print()    


#Q.write a python code to print a pyramid with stars and remove the middle stars in the pyramid?
a=5
for i in range(a):
    for j in range(i+1):
        if j==0 or i==a-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



#Q.write a code to form  regular triangle?
a=5
for i in range(a):
    for j in range(a-i):
        print(" ", end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()



#Q.write a python code to print reverse right angle triangle?
a=5
for i in range(a):
    for j in range(a-i):
        print("*",end=" ")
    print()



#Q.write a pythom code where the spaces after the forming of triangle should be &?
a=5
for i in range(a):
    for j in range(a-i):
        print("&", end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    for l in range(a-i):
        print("&",end=" ")
    print()




#Q.write a python code to form a reverse regular triangle?
a=5
for i in range(a-1,-1,-1):
    for j in range(a-i):
        print(" ", end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()

#without slicing:
a=5
for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range((a-i)*2-1):
        print("*",end=" ")
    print()


#Q.write a python code to add & in place of spaces in reverse triangle?
a=5
for i in range(a):
    for j in range(i+1):
        print("&", end=" ")
    for k in range((a-i)*2-1):
        print("*",end=" ")
    for l in range(i+1):
        print("&",end=" ")
    print()
    

#Q.write a code to form a diamond?
a=5
for i in range(a-1):
    for j in range(a-i):
        print(" ", end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()
for i in range(a):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range((a-i)*2-1):
        print("*",end=" ")
    print()



#Q.write a python code to print the timer symbol?
a=5
for i in range(a-1):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range((a-i)*2-1):
        print("*",end=" ")
    print()
for i in range(a):
    for j in range(a-i):
        print(" ", end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()




##Q.Traffic signal system input signal color. Red ->stop, Yellow-->ready, green --> go,otherwise invalid signal.
#do the problem with conditional statements.
signal=input("enter a signal colour:")
if signal=="red":
    print("STOP")
elif signal=="Yellow":
    print("READY")
elif signal=="green":
    print("GO")
else:
    print("INVALID SIGNAL")




#same previous problem using match:
signal=input("enter the signal:")
match signal:
    case "red":
        print("STOP")
    case "Yellow":
        print("READY")
    case "green":
        print("GO")
    case " ":
        print("INVALID SIGNAL")




#Q.write a python code to print numbers in words using match?
val=int(input("enter the val:"))
match val:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case " ":
        print("INVALID VALUE")


##while loop
#Q.printing even numbers using while?
val=int(input("enter val:"))
num=1
while num <=val:
    print(num)
    num+=2



##FUNCTIONS
#Q.printing even numbers using functions
def check_even():
    if num%2==0:
        print("even")
    else:
        print("odd")

num=int(input("enter a number:"))
check_even()


#Q.write a python code to print prime numbers?
def prime():
    if num%1==0 and num%num==0:
        print("prime")
    else:
        print("NOT PRIME")

num=int(input("enter a number:"))
prime()

#Q.check prime and not prime elements?
def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("PRIME")
    else:
        print("NOT PRIME")
num=int(input("enter a number:"))
check_prime(num)



#Q.MOVIE TICKET ELIGIBILITY
#input age: below 5 ->free entry,5-17 ->child ticket,18-59 -> Adult ticket, 60+ -> senior citizen Discount.
def eligibility(age):
    if age<=5:
        print("FREE ENTRY !!")
    elif age>5 and age<=17:
        print("CHILD TICKET")
    elif age>18 and age<=59:
        print("ADULT TICKET")
    elif age>=60:
        print("SENIOR CITIZEN DISCOUNT")
    else:
        print("INVALID AGE")

age=int(input("enter age:"))
eligibility(age)


##LIST:
#Q.
li=[1,2,3,4,5]
res=" "
ans=[]
for i in range(len(li)):
    ans.insert (0,li[i])
    res=str(li[i])+res

print(res)
print(ans)



###SET:
#Q.formate of set to be stored and it opperations
s=set()
s.add(1)
s.add(2)
s.add(1)# if the element already present it ignores but dont show any error
print(s)


#Q.add each and every element to the set
li=[1,2,3,1,2,3]
s=set(li)
print(s)


##DICTIONARY:
#key and values of a given list
li=[1,2,3,1,2,3]
dici={}
for i in range(len(li)):
    if li[i] in dici:
        dici[li[i]] +=1
    else:
        dici[li[i]]=1
print(dici)

for key,value in dici.items():
    print(key,value)


#dictionary with string
li=["ram","sam","mahesh","sonu","rahul","ram","sam","mahesh","sonu","sam"]
dici={}
for i in range(len(li)):
    if li[i] in dici:
        dici[li[i]] +=1
    else:
        dici[li[i]]=1
print(dici)

for key,value in dici.items():
    if value > 2:
        print(key,value)


#dictionary using functions:
def frequency_count(li):
    dici={}
    for i in range(len(li)):
        if li[i] in dici:
            dici[li[i]]+=1
        else:
            dici[li[i]]=1
    print(dici)
    for key,value in dici.items():
        if value>2:
            print(key,value)

li=["ram","sam","mahesh","sonu","rahul","ram","sam","mahesh","sonu","sam"]
frequency_count(li)
