# #brute force
# def fun(nums):
#     n=len(nums)
#     freq=[0]*(n+1)
#     for num in nums:
#             freq[num]+=1
#     repeating=-1
#     missing=-1
#     for i in range(1,n+1):
#         if freq[i]==2:
#             repeating=i
#         elif freq[i]==0:
#             missing=i
#     return [missing , repeating ]
# nums=[1,2,2,4]
# print(fun(nums))

#optimal 
def RM(nums):
    n=len(nums)
    E=n*(n+1)//2
    A=sum(nums)
    diff=A-E
    E_sqr=n*(n+1)*(2*n+1)//6
    A_sqr=sum(num*num for num in nums)
    sqr_diff=A_sqr-E_sqr
    sum_rm=sqr_diff//diff
    R=(diff+sum_rm)//2
    M=sum_rm-R
    return [R,M]
nums=[1,2,2,4]
print(RM(nums))
