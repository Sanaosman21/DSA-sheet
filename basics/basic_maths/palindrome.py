def Palindrome(n):
    original=n
    revNum=0
    while(n>0):
        ld=n%10
        revNum=(revNum*10)+ld
        n=n//10
    if (original==revNum):
        return True
    else:
        return False
print(Palindrome(7789))