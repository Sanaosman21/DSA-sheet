def printNumbers(n):
    if (n==1):
        return ;
    n-=1
    printNumbers(n)
    print(n)
printNumbers(5)


