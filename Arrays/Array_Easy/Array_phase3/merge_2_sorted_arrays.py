# Merge two Sorted Arrays Without Extra Space
# Problem Statement: Given two sorted integer arrays nums1 and nums2, merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# Array nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s whereas nums2 has a length of n.
# def mergearrays(nums1,nums2):

def mergearrays(nums1,nums2):
    m=len(nums1)
    n=len(nums2)
    nums1+=[0]*n
    i=m-1
    j=n-1
    k=m+n-1
    while j>=0 and i>=0:
        if nums2[j]>nums1[i]:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        else:
            nums1[k]=nums1[i]
            i-=1
            k-=1
    while j>=0:
        nums1[k]=nums2[j]
        j-=1
        k-=1
    return nums1
nums1=[1,2,2,3]
nums2=[4,4,5,6]
print(mergearrays(nums1,nums2))

