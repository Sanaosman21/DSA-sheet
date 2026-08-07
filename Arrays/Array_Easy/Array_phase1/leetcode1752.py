def fun(arr):
    n=len(arr)
    b=0
    for i in range(n):
        if arr[i]<arr[(i+1)%n]:
            continue
        else:
            b+=1
    if b<=1:
        return True 
    return False 
arr= [1,2,3]
print(fun(arr))