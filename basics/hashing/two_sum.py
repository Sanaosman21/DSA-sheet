def two_sum(arr,target): 
    dict={}
    for i in range(len(arr)+1):
        current_num=arr[i]
        needed=target-current_num
        if needed in dict:
            return [dict[needed],i]
        else:
            dict[current_num]=i
arr=[2,7,11,15]
print(two_sum(arr,9))
