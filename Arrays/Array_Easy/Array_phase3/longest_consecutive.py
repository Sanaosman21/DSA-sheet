def fun(nums):
  seen=set(nums)
  longest=0
  for num in seen:
    if num-1 not in seen:
        count=0
        while num in seen:
            count+=1
            num+=1
        if count>longest:
           longest=count
    return longest
nums=[100,4,200,1,3,2]
print(fun(nums))
