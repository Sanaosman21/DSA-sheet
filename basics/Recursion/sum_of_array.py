def fun(arr):
    if len(arr)==0:
        return 0;
    return 5+fun(arr[1:])
print(fun([5,8,2]))