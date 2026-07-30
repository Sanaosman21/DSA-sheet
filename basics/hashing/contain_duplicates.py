# def dup(arr):
#     freq=[0]*4
#     for num in arr:
#         if num in freq:
#             freq[num]+=1
#         else:
#             freq[num]=1
#     for num in freq:
#         if num>1:
#             return True
#         else:
#             return False 
# arr=[1,2,3,1]
# print(dup(arr))
def dup(arr):
    freq={}
    for num in arr:
        if num in freq:
            return True
        else:
            freq[num]=1
    return False
arr=[1,2,3,4,1]
arr2=[1,2,3,4]
print(dup(arr))
print(dup(arr2))