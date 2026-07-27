def countDigits(n):
    count=0
    while(n>0):
        lastdigit=n%10
        count=count+1
        n=n//10
    return count
print(countDigits(7783))