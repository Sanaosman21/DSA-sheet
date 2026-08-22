def fun(nums,k):
    lsum=sum(nums[0:k])
    max_sum=lsum
    rsum=0
    n=len(nums)
    r=n-1
    l=k-1
    for i in range(k):
        lsum-=nums[l]
        l-=1
        rsum+=nums[r]
        r-=1
        max_sum=max(max_sum,lsum+rsum)
    return max_sum
nums=[1,2,3,4,5,6,1]
print(fun(nums,3))