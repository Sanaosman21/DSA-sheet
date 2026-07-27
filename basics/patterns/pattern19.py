def pattern19(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        for j in range(2*i):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        for j in range(2*(n-i-2)+2):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
pattern19(5)
pattern2(5)
