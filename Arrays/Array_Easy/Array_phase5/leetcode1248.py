# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.
# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
def numberOfSubarrays(nums, k):
        count=0
        prefix_sum=0
        freq={0:1}
        for num in nums:
            if num%2==0:
                num=0
            else:
                num=1
            prefix_sum+=num
            needed=prefix_sum-k
            if needed in freq:
                count+=freq[needed]
            if prefix_sum not in freq:
                freq[prefix_sum]=1
            else:
                freq[prefix_sum]+=1
        return count
nums=[2,2,2,1,2,2,1,2,2,2]
print(numberOfSubarrays(nums,2))
