#brute force 
def fun(nums):
    n=len(nums)
    pos=[]
    neg=[]
    for i in range(len(nums)):#separating pos and neg numbers
        if nums[i]>=0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    result=[]
    for i in range(len(pos)):#merging neg and pos array
        result.append(pos[i])
        result.append(neg[i]) 
    print(pos)
    print(neg)   
    print("result through brute force",result)
nums= [3, 1, -2, -5, 2, -4]
fun(nums)

#optimal approach 
def rearrange(nums):
    n=len(nums)
    r=[0]*n
    pos_index=0
    neg_index=1
    for i in range(n):
        if nums[i]>0:
            r[pos_index]=nums[i]
            pos_index+=2
        else:
            r[neg_index]=nums[i]
            neg_index+=2
    print("result through optimal approach",r)
nums= [3, 1, -2, -5, 2, -4]
rearrange(nums)