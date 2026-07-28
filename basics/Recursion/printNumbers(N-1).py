def printNumbersrev(i,n):
    if (i<1):
        return;
    print(i)
    printNumbersrev(i-1,n)
printNumbersrev(5,5)