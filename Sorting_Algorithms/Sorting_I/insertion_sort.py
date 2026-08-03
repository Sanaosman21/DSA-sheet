def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    print("after sorting array")
    print(arr)
arr=[5,4,10,1,6,2]
insertion_sort(arr)
