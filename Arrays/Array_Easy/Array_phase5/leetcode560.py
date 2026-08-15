def subarray(nums,k):
    prefix={0:1}
    sum=0
    count=0
    for i in range(len(nums)):
        sum+=nums[i]
        needed=sum-k
        if needed in prefix:
            count+=prefix[needed]
        if sum not in prefix:
            prefix[sum]=i
    return count
nums=[1,2,3,1,1,1,1]
print(subarray(nums,3))