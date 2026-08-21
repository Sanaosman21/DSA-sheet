# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
# Example 1:
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
def numberOfSubarrays(nums,k,thershold):
    window_sum=sum(nums[0:k])
    count=0
    if window_sum>=k*thershold:
        count+=1
    l=0
    r=k-1
    while(r<len(nums)-1):
        window_sum-=nums[l]
        l+=1
        r+=1
        window_sum+=nums[r]
        if window_sum>=k*thershold:
            count+=1
    return count
nums=[2,2,2,2,5,5,5,8]
print(numberOfSubarrays(nums,3,4))