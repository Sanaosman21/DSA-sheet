arr=[1,2,3,2,2,1]
freq={}
max_freq=0
ans=0
for element in arr:
    if element in freq: 
        freq[element]+=1
    else :
        freq[element]=1
for element , current_freq in freq.items():
    if current_freq > max_freq or (current_freq == max_freq and element < ans):  
        max_freq=current_freq
        ans=element 
    
print(f"{ans} has highest frequnecy of {max_freq}")
        
