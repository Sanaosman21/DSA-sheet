def subarraysDivByK(nums,k) :
        freq={0:1}
        prefix_sum=0
        count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            r=prefix_sum % k
            if r in freq:
                count+=freq[r]
            if r not in freq:
                freq[r]=1
            else:
                freq[r]+=1
        return count
nums=[4,5,0,-2,-3,1]
print(subarraysDivByK(nums,5))