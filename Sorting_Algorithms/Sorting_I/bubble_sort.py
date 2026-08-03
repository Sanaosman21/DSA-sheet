def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swap=False
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        swap=True
        if not swap:
            break;
    print("after sorting")
    print(arr)
arr=[13,24,46,52,20,9]
arr1=[1,2,3,4]
bubble_sort(arr1)
            