def sumFunctional(n):
    if (n==0):
        return 0;
    return n+sumFunctional(n-1)
print(sumFunctional(4))