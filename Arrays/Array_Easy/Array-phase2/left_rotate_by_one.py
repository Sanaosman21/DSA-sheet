#optimal approach 
def fun(nums):
    if len(nums)==0:
        return 
    temp=nums[0]
    for i in range(len(nums)-1):
        nums[i]=nums[i+1]
    nums[-1]=temp
    return nums
nums=[1,2,3,4,5]
print(fun(nums))

