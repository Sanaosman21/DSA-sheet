arr1=[4,9,5]
arr2=[9,4,9,8,4]
new_arr=[]
for i in arr1:
    for j in arr2:
        if i==j:
            if i  not in new_arr:
                new_arr.append(i)
print(new_arr)

