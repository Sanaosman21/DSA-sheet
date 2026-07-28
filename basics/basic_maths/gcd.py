def Gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a 
print(Gcd(48,18))