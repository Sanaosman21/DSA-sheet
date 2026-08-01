#BRUTE FORCE APPROACH
# def fun(arr,k):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#           if arr[i]==arr[j]:
#              if j-i<=k:
#                 return True 
#     return False 
def fun(arr,k):
    seen={}
    for i in range(len(arr)):
        num=arr[i]
        if num in seen:
            old_index=seen[num]
            d=i-old_index
            if d<=k:
                return True
            seen[num]=i #update index
        else:
            seen[num]=i
    return False 
arr=[1,0,1,1] 
print(fun(arr,1)) 

# Contains Duplicate II (LeetCode 219) — Hashing Pattern Notes

## Problem Pattern:

# **Hashing + Index Tracking**

# When a problem asks:

# * Have I seen this element before?
# * How close are the duplicate elements?
# * Need the position/index of previous occurrence?

# Use a dictionary.

# ---

# ## Key Idea:

# A set only stores:

# ```
# value
# ```

# Example:

# ```
# {1,2,3}
# ```

# It can tell:
# "Have I seen this number?"

# But we need:

# "Where did I see this number?"

# So use a dictionary:

# ```
# value : index
# ```

# Example:

# ```
# {
#   1:0,
#   2:1,
#   3:2
# }
# ```

# Meaning:

# * 1 was seen at index 0
# * 2 was seen at index 1
# * 3 was seen at index 2

# ---

# ## Algorithm:

# 1. Create an empty dictionary.

# ```
# seen = {}
# ```

# 2. Traverse the array using index.

# ```
# for i in range(len(nums)):
# ```

# 3. Take the current value:

# ```
# num = nums[i]
# ```

# 4. Check if the number already exists:

# ```
# if num in seen:
# ```

# If yes:

# * Get previous index:

# ```
# old_index = seen[num]
# ```

# * Calculate distance:

# ```
# distance = i - old_index
# ```

# * Check:

# ```
# distance <= k
# ```

# If true:

# ```
# return True
# ```

# 5. Update the latest index:

# ```
# seen[num] = i
# ```

# Why update?

# Because the closest previous occurrence is always useful.

# ---

# ## Important Difference:

# ### Frequency Hashing

# Used when we need counts:

# ```
# character : frequency
# ```

# Example:

# ```
# {
# 'a':3,
# 'b':2
# }
# ```

# ---

# ### Index Hashing

# Used when we need positions:

# ```
# value : index
# ```

# Example:

# ```
# {
# 5:0,
# 8:3
# }
# ```

# ---

# ## Why update index?

# Example:

# ```
# nums = [1,0,1,1]
# k = 1
# ```

# First 1:

# ```
# seen = {1:0}
# ```

# Second 1:

# Distance:

# ```
# 2 - 0 = 2
# ```

# Not valid.

# Update:

# ```
# seen = {1:2}
# ```

# Third 1:

# Distance:

# ```
# 3 - 2 = 1
# ```

# Valid.

# ---

# ## Complexity:

# Time Complexity:

# ```
# O(n)
# ```

# Because we traverse the array once.

# Dictionary operations:

# ```
# insert → O(1)
# search → O(1)
# update → O(1)
# ```

# Space Complexity:

# ```
# O(n)
# ```

# Because dictionary can store every unique element.

# ---

# ## Interview Pattern Recognition:

# If you see:

# "duplicate"
# "within k distance"
# "nearby"
# "last occurrence"
# "previous position"

# Think:

# ```
# Dictionary → value:index
# ```


        
            


        

            
    
