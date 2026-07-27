def pattern20(n):
    spaces=2*n-2
    for i in range(1,2*n):      
        if i<=n:
            stars=i
        else:
            stars=2*n-i
        print("*"*stars,end=" ")
        print(" "*spaces,end=" ")
        print("*"*stars,end=" ")
        if i<n:
            spaces-=2
        else:
            spaces+=2
        print()

pattern20(5)