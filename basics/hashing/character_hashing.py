s=input("enter the string: ")
freq=[0]*26
for char in s:
    index=ord(char)-ord("a")
    freq[index]+=1
#fetching 
q=int(input("enter the number of queries: "))
for _ in range(q):
    character=input("enter the character: ")
    index=ord(character)-ord("a")
    print(freq[index])