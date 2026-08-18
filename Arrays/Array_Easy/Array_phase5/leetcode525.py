def fun(nums):
    n=len(nums)
    prefix={0:-1}
    prefix_sum=0
    max_len=0
    for i in range(n):
        if nums[i]==0:
            prefix_sum-=1
        else:
            prefix_sum+=1
        if prefix_sum in prefix:
            length=i-prefix[prefix_sum]
            max_len=max(length,max_len)
        elif prefix_sum not in prefix:
            prefix[prefix_sum]=i
    return max_len
nums=[0,1,1,1,1,1,0,0,0]
print(fun(nums))