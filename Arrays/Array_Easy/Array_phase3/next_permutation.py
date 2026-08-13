def nextper(nums):
    pivot=-1
    for i in range(len(nums)-1,0,-1):
        if nums[i-1]<nums[i]:
            pivot=i-1
            break
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[pivot]:
            nums[i],nums[pivot]=nums[pivot],nums[i]
            break
    l=pivot+1
    r=len(nums)-1
    while(l<r):
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    return nums
nums=[1,2,3]
print(nextper(nums))