#BRUTE FORCE APPROACH
# def fun(arr,k):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#           if arr[i]==arr[j]:
#              if j-i<=k:
#                 return True 
#     return False 
def fun(arr,k):
    seen={}
    for i in range(len(arr)):
        num=arr[i]
        if num in seen:
            old_index=seen[num]
            d=i-old_index
            if d<=k:
                return True
            seen[num]=i
        else:
            seen[num]=i
    return False 
arr=[1,0,1,1] 
print(fun(arr,1)) 

        
            


        

            
    
