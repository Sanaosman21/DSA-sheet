def pattern5(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(j ,end=" ")
        print()
res=pattern5(5)
print(res)