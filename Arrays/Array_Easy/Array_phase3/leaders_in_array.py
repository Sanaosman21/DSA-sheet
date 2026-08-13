def leaders(nums):
    leader=[]
    max=nums[len(nums)-1]
    leader.append(max)
    for i in range(len(nums)-2,0,-1):
       if nums[i]>max:
           max=nums[i]
           leader.append(max)
    leader.reverse()
    return leader
nums=[4,7,1,0]
nums1=[16,17,4,3,5,2]
print(leaders(nums1))
            
