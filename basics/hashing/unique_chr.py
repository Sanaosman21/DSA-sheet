def fun(str):
    freq={}
    for ch in str:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    index=0
    for ch in str:
        if freq[ch]==1:
            return index
        index+=1
    return  -1
print(fun("aabbc"))