#optimal approach with the tc of sqrt(n)
from math import sqrt
def isPrime(n):
    if (n<=1):
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True
print(isPrime(9))

