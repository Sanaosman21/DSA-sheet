arr=[1,1,2,4,5]
hash_arr=[0]*6
for num in arr:
    hash_arr[num]+=1
#fetching 
q=int(input("enter the number of quries"))
for _ in range(q):
    number=int(input("enter the number"))
    print("frequency of number is ",hash_arr[number])
