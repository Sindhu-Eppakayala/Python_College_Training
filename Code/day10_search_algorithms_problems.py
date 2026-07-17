# day10_search_algorithms_problems

#LINEAR SEARCH
#def: finding  the linear element from each element
arr=[1,2,3,4,5]
target=4
for i in range(len(arr)):
    if target==arr[i]:
        print(i)


##BINARY SEARCH:
nums=[-1,0,3,5,9,12]
target=9
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if nums[mid]==target:
        print(mid)
        break
    elif target>nums[mid]:
        l=mid+1
    else:
        r=mid-1
 
#Q.arr[-1,0,3,5,7,8,10]find the index where we can insert a new element.element we area dding in the above array is not there in the array?
#Target=2
def binarysearch(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif target >nums[mid]:
            l=mid+l
        else:
            r=mid-1
    return l
nums=[-1,0,3,5,7,8,12]
target=10
print(binarysearch(nums,target))
    


##Q.given an array of character sorted in ascending order,find the greatest character that is less than the target character in the array. target character is not present in the array
#if there is not such element return 'a'
#{'c','e','g','k','y'} target="f"
def binary_search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
       mid=(l+r)//2

       if nums[mid]==target:
        print(mid)
        break
       elif target>nums[mid]:
        l=mid+1
       else:
        r=mid-1
    return nums[r]
nums=['c','e','g','k','y']
target='f'
print(binary_search(nums,target))  



#Q.find the index of 2 where to be inserted?
def binary_Search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            l=mid+1
        elif target>nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return r
nums=[1,2,2,2,2,3]
target=2
print(binary_Search(nums,target))


#q.find the index of the 
def binary_search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
       mid=(l+r)//2

       if nums[mid]>=target:
        print(mid)
        break
       elif target>nums[mid]:
        l=mid+1
       else:
        r=mid-1
    return nums[r]
nums=['c','e','g','k','y']
target='f'
print(binary_search(nums,target))       




#Q.finf the left most and right most value of 8?
#s=[5,7,7,8,8,10],target=8
def binary_Search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            l=mid+1
        elif target>nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return nums[l,r]
nums=[5,7,7,8,8,10]
target=8
print(binary_Search(nums,target))

##Leetcode Q.2529
nums=[-3,-2,-1,0,0,1,2]
positive=0
negative=0
for i in range(len(nums)):
    if nums[i]<0:
        positive+=1
    elif nums[i]>0:
        negative +=1
    else:
        positive=0
        negative=0
    if positive>negative:
        max=positive
    else:
        max=negative
print(max)


##BUBBLE SORT:
nums=[7,12,9,11,3]
for i in range(len(nums)):
    swap=False
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swap=True
    if not swap:
        print("Sorted")
        break    
print(nums)


nums=[1,3,4,2,2]
count=0
dici={}
for num in range(nums):
    if nums[i]==dici:
        count+=1
        print(count)
if count>1:
    print(i)
