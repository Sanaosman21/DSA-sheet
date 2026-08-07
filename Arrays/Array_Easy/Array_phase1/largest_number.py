def fun(arr):
    largest=arr[0]
    for i in arr[1:]:
        if i>largest:
            largest=i
    return largest 
arr=[10, 20, 20, 5]
print(fun(arr))