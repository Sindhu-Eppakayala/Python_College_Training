# Day08_sliding_window_problems

arr=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(arr)):
    temp=arr[i]
    for j in range(len(temp)):
        print(arr[i][j],end=" ")
    print()



arr=[[1,2,3,4],[4,5,6,7],[7,8,9,5]]
for i in range(len(arr)):
    temp=arr[i]
    for j in range(len(temp)):
        print(arr[i][j],end=" ")
    print()



arr=[[1,2,3,4],[4,5,6,7],[7,8,9,5]]
print(arr[0][0])
#1st 0 is 0th position of 1st array =[1,2,3,4]
#2nd 0 is 0th position of the 1st array 1


arr=[1,1,5,4,6,3,9,9]
l=float("-inf")
sl=float("-inf")
for i in range(len(arr)):
    if arr[i]>l:
        sl=l
        l=arr[i]
    elif arr[i]>sl and arr[i] !=l:
        sl=arr[i]
print(l)
print(sl)


arr=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans=0
for i in range(len(arr)):
    temp=arr[i]
    count=0
    for j in range(len(temp)):
        if temp[j]== " ":
            count+=1
    ans=max(ans,count)
print(ans)


##Sliding window

n=[5,9,1,8,7]
for i in range(len(n)):
    for j in range(i,len(n)):
        temp=[]
        for k in range(i,j+1):
            temp.append(n[k])
        if len(temp)==3:
            print(temp,sum(temp))
        print()



nums=[5,9,1,8,7]
ans=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        a=[]
        for k in range(i,j+1):
            a.append(nums[k])
        if len(a)==3:
            ans=max(ans,sum(a))
print(ans)


s="XYZZAZ"
k=3
temp=0
l=0
ans=0
for r in range(len(s)):
    temp+=s[r]
    if r-l==k:
        temp-=s[l]
        l+=1
    ans=max(ans,temp)
    if r-l+1==k:
        print(s[l:r+1],sum(s[l:r+1]))
print(ans)
    
