# iven an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
# Example 1
# Input: nums = [0, 2, 3, 1, 4]
# Output: 5
# Explanation:
# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
# Example 2
# Input: nums = [0, 1, 2, 4, 5, 6]
# Output: 3
# Explanation:
# nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]
#using math 
def fun(nums):
    n=len(nums)
    expected=n*(n+1)//2
    actual=sum(nums)
    missing=expected-actual
    return missing
nums=[3,0,1]
print(fun(nums))

# using XOR
def missing(nums):
    n=len(nums)
    xor=0
    for i in range(n+1):
        xor=xor^i
    for num in nums:
        xor=xor^num
    return xor
nums=[3,0,2]
print(missing(nums))