def bubble_Sort(arr,n):
    if n==0:
        return
    swaped=False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swaped=True
    if not swaped:
        return None
    bubble_Sort(arr,n-1)
arr=[1,2,3,4]
bubble_Sort(arr, len(arr))
print("after sorting")
print(arr)