#brute force
def fun(nums):
    n=len(nums)
    freq=[0]*(n+1)
    for num in nums:
            freq[num]+=1
    repeating=-1
    missing=-1
    for i in range(1,n+1):
        if freq[i]==2:
            repeating=i
        elif freq[i]==0:
            missing=i
    return [missing , repeating ]
nums=[1,2,2,4]
print(fun(nums))
