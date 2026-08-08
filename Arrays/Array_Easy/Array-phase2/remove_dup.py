def fun(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1
arr=[1, 1, 2, 2, 3]
k=fun(arr)
print(k)
print("unique elements are",arr[:k])

#here i is the writing pointer and j is the reading pointer 
