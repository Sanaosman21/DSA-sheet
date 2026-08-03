def insertion_sort(arr,n):
    if n<=1:
        return 
    insertion_sort(arr,n-1)
    temp=arr[n-1]
    j=n-2
    while (j>=0 and arr[j]>temp):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=temp
    
arr=[5,4,10,1,6,2]
insertion_sort(arr,len(arr))
print(arr)
