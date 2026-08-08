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

# ⭐ Pattern Recognition

# Whenever you see:

# Rotate by One
# Shift Left
# Shift Right

# Think:

# Save the element that will be overwritten.
# Shift remaining elements.
# Put the saved element in its final position.

# This is the core idea behind rotation problems.