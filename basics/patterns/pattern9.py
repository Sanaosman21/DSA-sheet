def pattern1(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()
def pattern2(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        for j in range(i):
            print(" ",end="")
        print()
pattern1(5)
pattern2(5)