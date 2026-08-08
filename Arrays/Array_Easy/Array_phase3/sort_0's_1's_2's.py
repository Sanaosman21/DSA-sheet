# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
#brute force 
def fun(nums):
    count0=count1=count2=0
    for num in nums:
        if num==0:
            count0+=1
        elif num==1:
            count1+=1
        elif num==2:
            count2+=1
    index=0
    for _ in range(count0):
        nums[index]=0
        index+=1
    for _ in range(count1):
        nums[index]=1
        index+=1
    for _ in range(count2):
            nums[index]=2
            index+=1
    return nums
nums = [1, 0, 2, 1, 0]
print(fun(nums))

#better appraoch 
def fun1(nums):
    count0=count1=count2=0
    for num in nums:
        if num==0:
            count0+=1
        elif num==1:
            count1+=1
        count2+=1
    for i in range(count0):
        nums[i]=0
    for i in range(count0,count0+count1):
        nums[i]=1
    for i in range(count0+count1,len(nums)):
        nums[i]=2
    return nums
nums = [1, 0, 2, 1, 0]
r=fun1(nums)
print("nums by better appraoch",r)
nums = [1, 0, 2, 1, 0]
print(fun(nums))

#optimal approach 
def sort(nums):
    low=mid=0
    high=len(nums)-1
    while(mid<high):
        if nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
        elif nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
    return nums
nums=[2,0,1,1,2,0]
print("by optimal approach",sort(nums))
        
