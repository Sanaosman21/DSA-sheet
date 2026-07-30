def fun(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    n=len(arr)
    for num in freq:
        if freq[num]>n/2:
            return num
    return None
arr=[1,2,3,4]
print(fun(arr))