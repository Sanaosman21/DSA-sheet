# 🪟 Question 1: Longest Subarray with Given Sum K
# Example
# nums = [1, 2, 3, 1, 1, 1, 1]
# k = 5
# We need the longest contiguous subarray whose sum is 5.
def fun(nums,k):
    l=0
    r=0
    maxlen=0
    window_sum=0
    for r in range(len(nums)):
        window_sum+=nums[r]
        while(window_sum>k):
            window_sum-=nums[l]
            l+=1
        if window_sum==k:
            length=r-l+1
            maxlen=max(maxlen,length)
    return maxlen
nums=[1, 2, 3, 1, 1, 1, 1]
print(fun(nums,5))