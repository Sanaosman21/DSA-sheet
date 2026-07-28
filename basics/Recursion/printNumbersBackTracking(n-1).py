def printNumbers(i,n):
    if(i>n):
        return 
    printNumbers(i+1,n)
    print(i)
printNumbers(1,5)