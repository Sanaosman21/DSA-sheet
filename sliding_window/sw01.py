def fun(nums,k):
    window_sum=sum(nums[0:k])
    max_sum=window_sum
    l=0
    r=k-1
    n=len(nums)
    while(r<n-1):
        window_sum-=nums[l]
        l+=1
        r+=1
        window_sum+=nums[r]
        max_sum=max(window_sum,max_sum)
    return max_sum 
nums=[2, 1, 5, 1, 3, 2]
nums2=[4, 2, 1, 7, 8, 1, 2]
print(fun(nums2,3))
