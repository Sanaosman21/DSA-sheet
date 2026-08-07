#Brute force approach 
# def fun(arr):
#         temp=[0]*len(arr)
#         index=0
#         for num in arr:
#             if num!=0:
#                 temp[index]=num
#                 index+=1
#         for i in range(len(arr)):
#             arr[i]=temp[i]
#         return arr
 
# arr = [0, 1, 0, 3, 12]
# print(fun(arr))

#optimal approach 
def fun(arr):
    j=-1
    for i in range(len(arr)):
        if arr[i]==0:
            j=i
            break
    if j==-1:
        return   
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr 
arr=[0,1,0,3,12]
print(fun(arr))

    