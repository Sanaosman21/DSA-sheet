# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
def numSubarraysWithSum(nums ,goal):
        total=0
        freq={0:1}
        count=0
        for num in nums:
            total+=num
            needed=total-goal
            if needed in freq:
                count+=freq[needed]
            if total not in freq:
                freq[total]=1
            else:
                freq[total]+=1
        return count
nums=[1,0,1,0,1]
print(numSubarraysWithSum(nums,2))