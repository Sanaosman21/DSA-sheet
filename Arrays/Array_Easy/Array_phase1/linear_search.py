def fun(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
arr=[4, 7, 2, 9, 5]
print(fun(arr,8))
    