#optimal 
def subarray(nums,k):
    prefix={0:-1}
    sum=0
    max_len=0
    for i in range(len(nums)):
        sum+=nums[i]
        needed=sum-k
        if needed in prefix:
            length=i-prefix[needed]
            max_len=max(max_len,length)
        if sum not in prefix:
            prefix[sum]=i
    return max_len
nums=[1,2,3,1,1,1,1]
print(subarray(nums,3))
