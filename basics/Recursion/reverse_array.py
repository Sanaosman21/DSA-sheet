#using two varibales
def fun(arr,l,r):
    if l>=r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    fun(arr, l+1,r-1)
arr=[1,2,3,4]
fun(arr,0,len(arr)-1)
print(arr)

# using single variable 
def fun2(arr,i):
    if i>=len(arr)//2:
        return 
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    fun2(arr,i+1)
arr=[4,5,6,7,8]
fun2(arr,0)
print(arr)