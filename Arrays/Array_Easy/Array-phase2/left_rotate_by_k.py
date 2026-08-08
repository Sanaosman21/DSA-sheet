#Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.
#brute force approach 
def leftrotate(nums,k):
    n=len(nums)
    k=k%n
    temp=nums[:k]
    remaining=nums[k:]
    nums=remaining+temp
    print(nums)
leftrotate([1,2,3,4,5],2)

#optimal approach  //IF DIRECTION IS LEFT
def reverse(nums,start,end):
    while(start<end):
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
# def right_rotate(nums,k):

def rotateArray(nums,k,Direction):
    n=len(nums)
    if k==0 or n==0:
        return nums
    k=k%n
    if (Direction=='left'):
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
        reverse(nums,0,n-1) 
    
    if (Direction=='right'):
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
    return nums
nums=[1,2,3,4,5]
k=2
print(rotateArray(nums,k,'right'))
