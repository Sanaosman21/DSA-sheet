arr=[4,4,6,7,8]
freq={}
min_freq=9999
ans=0
for element in arr:
    if element in freq:
        freq[element]+=1
    else:
        freq[element]=1
for element ,key in freq.items():
    if key<min_freq:
        min_freq=key
        ans=element 
print(f"freq of {ans} is {min_freq}")