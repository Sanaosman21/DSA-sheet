#print numbers from 1 to n
# def printNumbers(i,n):
#     if (i>n):
#         return;
#     print(i)
#     printNumbers(i+1,n)
# printNumbers(0,5)

# print from n to 1
def printNumbersrev(i,n):
    if (i<1):
        return;
    print(i)
    printNumbersrev(i-1,n)
printNumbersrev(5,5)