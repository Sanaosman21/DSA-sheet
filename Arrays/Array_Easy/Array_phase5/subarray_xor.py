# Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

# Note: It is guranteed that the total count will fit within a 32-bit integer.

# Examples: 

# Input: arr[] = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
# Input: arr[] = [5, 6, 7, 8, 9], k = 5
# Output: 2
# Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
# Input: arr[] = [1, 1, 1, 1], k = 0
# Output: 4
# Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
def subarray(nums,k):
    count=0
    freq={0:1}
    current=0
    for num in nums:
        current^=num
        needed=current^k
        if needed in freq:
            count+=freq[needed]
        if current not in freq:
            freq[current]=1
        else:
            freq[current]+=1
    return count
nums=[4, 2, 2, 6, 4]
print(subarray(nums,6))
