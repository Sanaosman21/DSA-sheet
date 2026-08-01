arr1=[4,9,5]
arr2=[9,4,9,8,4]
s=set()
ans=set()
for i in arr1:
    s.add(i)
for i in arr2:
    if i in s:
       ans.add(i)
print(ans)