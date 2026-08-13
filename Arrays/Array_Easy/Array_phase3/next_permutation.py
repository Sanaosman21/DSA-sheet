# NEXT PERMUTATION
# Goal: smallest possible increase
#
# 1. Find pivot       → nums[i-1] < nums[i]
# 2. Find next greater → scan right → left
# 3. Swap
# 4. Reverse suffix
#
# Think: Pivot → Greater → Swap → Reverse


def nextper(nums):
    # 1️ Find pivot:
    # Scan from right → left.
    # Find first nums[i-1] < nums[i].
    # pivot = i-1
    # This is the position we need to increase.
    pivot=-1
    for i in range(len(nums)-1,0,-1):
        if nums[i-1]<nums[i]:
            pivot=i-1
            break
    #2Find the smallest number greater than pivot:
    # Scan from right → left.
    # First nums[i] > nums[pivot] is the one we need.
    # Swap pivot with it.
    if pivot!=-1:
         for i in range(len(nums)-1,0,-1):
             if nums[i]>nums[pivot]:
                 nums[i],nums[pivot]=nums[pivot],nums[i]
                 break
      # 3️ Reverse the suffix:
    # Everything after pivot is in descending order.
    # Reverse it to get the smallest possible suffix.
    l=pivot+1
    r=len(nums)-1
    while(l<r):
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    return nums
nums=[1,1,5]
print(nextper(nums))
