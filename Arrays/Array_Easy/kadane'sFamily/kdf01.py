# Kadane's Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.
def kadaneAlgo(nums):
    max=nums[0]
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum>max:
            max=sum
        if sum<0:
            sum=0
    return max
nums=[-2, 1, -3, 4, -1, 2, 1]
print(kadaneAlgo(nums))