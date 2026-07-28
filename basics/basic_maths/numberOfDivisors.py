from math import sqrt 
# def numberOfDivisors(n):
#     list=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list.append(i)
#     return list
# print(numberOfDivisors(24))
# // optimise solution with the tc of sqrt 
def numberOfDivisors(n):
    list=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            list.append(i)
            pair=n//i
        if pair!=i:
            list.append(pair)
    list.sort()
    return list 
print(numberOfDivisors(36))
print("tc is sqrt(n)")        
    