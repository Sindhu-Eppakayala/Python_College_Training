# Day09_sliding_window_and_basics

nums=[5,9,1,8,7]
k=3
l=0
ans=0
maxi=0
for r in range(len(nums)):
    ans+=nums[r]
    if r-l==3:
        ans-=nums[l]
        l+=1
    maxi=(max(maxi,ans))
print(maxi)



def countgoodstrings(self,s: str) -> int:
    l=0
    ans={}
    res=0
    for r in range(len(s)):
        if s[r] in ans:
            ans[s[r]]+=1
        else:
            ans[s[r]]=1
        if r-1==3:
            ans[s[l]]-=1
            if ans[s[l]]==0:
                ans.pop(s[l])
            l+=1
        if len(ans)==3 and r-l+1==3:
            res+=1
    return res



nums=[9,4,1,7]
k=2
mini=float("-inf")
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]>nums[j]:
            temp=nums[i]-nums[j]
        else:
            temp=nums[j]-nums[i]
        mini=min(mini,temp)
print(mini)
        




n=int(input("enter a number:"))
m=n*n*n

for i in range(m-1,-1,-1):
    for j in range(m-i):
        print("-",end=" ")
    print()

    
for i in range(5):
    for j in range(5):
        print(" ",end=" ")
    for k in range(i*2+1):
        print(".|.",end=" ")
    print()




n=int(input("enter a number:"))
m=3*n
for i in range(n):
    for j in range(m):
        print("-",end=" ")
    print()

a=5
for i in range(a):
    for j in range(a-i+2):
        print("-", end=" ")
    for k in range(a-i*3):
        print(".",end=" ")
    print()
