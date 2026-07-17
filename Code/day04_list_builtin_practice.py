# Day04_list_builtin_practice

###LIST:
#Q.write a python program for finding maximum element?
input=input("enter the set of list:")
a=int(list(input))
print(a)
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)

#CODE-1:
n=int(input("enter number of elements:"))
a=[]
for i in range(n):
    element=int(input("enter elements:"))
    a.append(element)
print(a)
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)



#CODE-2:
num=[2,3,4,5,6,7]
max=num[0]
for i in range(len(num)):
    if num[i]>max:
        max=num[i]
print("max:",max)


T.C=O(n)
#1st ieration is done for to find len(num) and its complexit is O(1)--->best case
#2nd iteration is done to compare the all the elements is O(n)--->worst case
#O(1)+O(n)--->O(n)
#o(space)=


#Q. write a python code for finding minimum elements?
n=int(input("enter number of elements:"))
a=[]
for i in range(n):
    element=int(input("enter elements:"))
    a.append(element)
print(a)
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)



#Q.write a python code for finding second maximum element?
n=int(input("enter number of elements:"))
a=[]
for i in range(n):
    element=int(input("enter elements:"))
    a.append(element)
print(a)
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)
for i in a:
    if max!=second_max:
        second_max=max
print(max)



#CODE-2
num=int(input("enter number of elements:"))
a=[]
for i in range(num):
    element=input("enter elements:")
    a.append(element)
print(a)
max=num[0]
sec_max=num[0]
for i in range(len(num)):
    if num[i]>max:
        sec_max=max
        max=num[i]
    elif num[i]>sec_max and num[i]!=max:
        sec_max=num[i]
print("max:",max)
print("sec max:",sec_max)


#CODE-3
num=[4,62,78,34,90]
max=num[0]
for i in num:
    if i > max:
        max=i

second_max=0
for i in num:
    if i!=max:
        if i > second_max:
            second_max=i
print("Maximum element:", max)
print("Second maximum element:", second_max)



# for loop is running once to find the length and another for internal comparisions
# T.C: O(n)+O(n)=O(n)
# space complexity=O(n)

# SEARCHING ALGORITHM:
#Q.write a python code to find a given element is present or not?
#TEST DATA:
#enter the elements:2 3 4 5 6 7
#Output:
#Target: 5
#5 is present at 3

#CODE-1:
num=int(input("enter target:"))
a=[]
for i in range(num):
    element=int(input("enter elements:"))
    a.append(element)
print(a)
for i in a:
    if i==num:
       #print(a.index(num)) 
       print(f'{num} is present at {a.index(num)}')
else:
    print("ELEMENT NOT FOUND")




#CODE-2:
num=list(map(int,input("elements:").split()))
target=int(input("Target:"))
for i in range(len(num)):
    if num[i]==target:
        print("present:",i)
        break
else:
    print("element not found")




#Q.finding the target element with index and position?
num=list(map(int,input("elements:").split()))
target=int(input("Target:"))
for i in range(len(num)):
    if num[i]==target:
        print("present in index:",i)
        print("position:",i+1)
        break
else:
    print("element not found")



#Q.write a python code for finding even numbers?

#CODE-1
num=list(map(int,input("enter the list:").split()))
print(num)
a=[]
for i in num:
    if i%2==0:
        a.append(i)
print(a)

#CODE-2:
num=list(map(int,input("enter the list:").split()))
even=[]
for i in range(len(num)):
    if num[i]%2==0:
        even.append(num[i])
print(even)



#Q.write a python program to print all odd numbers?
#CODE-1
num=list(map(int,input("enter the list:").split()))
print(num)
a=[]
for i in num:
    if i%2!=0:
        a.append(i)
print(a)

#CODE-2:
num=list(map(int,input("enter the list:").split()))
odd=[]
for i in range(len(num)):
    if num[i]%2==0:
        odd.append(num[i])
print(odd)



#Q.write a python code to return total count of even numbers in a list?
num=list(map(int,input("enter the list:").split()))
print(num)
a=[]
count=0
for i in num:
    if i%2==0:
        a.append(i)
        count+=1
print(a)
print(count)



#Q.write a python code to find the middle element?
#TEST DATA:
#enter the element:1 2 3 4 5 6
#OUTPUT:3
#a=int(input("enter a list:"))
input=input("enter the set of list:")
a=list(input)
print(a)
#a=list(map(int,input("enter the list elements:").split()))
length=len(a)
print("length of the list :",length)
mid=length//2
print("index of middle term is: ",mid)
print("the middle element is:",a[mid])




#LEETCODE PROBLEMS:
#Q.Given an array of integers nums and an integer target ,return indices of the 2 numbers such that they add up to target.
#you may assume that each input would have exactly one solution
#input:nums=[3,2,4],target=6
#output=[1,2]
nums=[2,7,11,15]
target=9
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print( [i,j])

T.C=n+n=7
n*n=n^2


#Q.write a python ciode to find sum of all listed elements
#TEST DATA:
#enter the elements: 1 2 3 4 5
#sum=15
num=list(map(int,input("enter the list:").split()))
print(num)
a=[]
count=0
for i in num:
        count+=i
print("sum:",count)



#Q.write a short program that prints each number from 1 to 100 on a new line.
#for each multiple of 3,print "Fizz" instead of the number.
#for eachmultiple of 5, print "Buzz" instead of the number.
#for numbers which are multipes of both 3 and 5,print "FizzBuzz" instead of number.
#write a solution(or reduce an existing one) so it has as few characters as possible.
for i in range(1,101):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)

#using list code for previous question:

mul=[]
for i in range(1,101):
    if i%3==0:
        mul.append("Fizz")
    elif i%5==0:
        mul.append("Buzz")
    elif i%3==0 and i%5==0:
        mul.append("FizzBuzz")
    else:
        mul.append(i)
print(mul)



#Q.A teacher asks the class to open their books to a page number. a student can eith start turning pages from the front of the book or from the back of the book.
#they always turn pages one at a time. when they open the book. page 1 is always on the right side:
#when they flip page 1, they see pages2 and 3.each page expect the last page will always be printed on both sides. the last page may only be printed on the front. given the length of the book. if the book is n pages long and a student wants to turn to page p. what is the minimum number of pages to turn? they can start at the beginning or the end of the book.
#given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.
n=int(input("enter number of pages in a book:"))
p=int(input("enter page to be opened:"))
present=int(input("enter the present page number opened:"))
for i in range(n):
    start_turn=p-present
print("if the pages start from front:",start_turn)
for i in range(n):
    end_turn=n-p
print("if the pages start from back:",end_turn)



#Q.write a python code for count how many times a number appeares?
#TEST DATA:
#elements:2 3 4 2
#OUTPUT:2'2 3'1 4'1
n=list(map(int,input("enter the list:").split()))
print(n)
a={}
for i in n:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print([a])
