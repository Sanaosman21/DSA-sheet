def isArmstrong(n):
    count=0
    original=n 
    sum=0
    while(n>0):
        count=count+1
        n=n//10
    n=original
    while(n>0):
        sum=sum+(n%10)**count
        n=n//10
    return sum==original
print(isArmstrong(144))