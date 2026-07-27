def pattern17(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        ch=ord('A')
        breakpoint=(2*i+1)//2
        for j in range(2*i+1):
            print(chr(ch),end=" ")
            if (j<breakpoint) :
                ch+=1
            else:
                ch-=1
        for j in range(n-i-1):
            print(" ",end=" ")
        print()
pattern17(5)
    
            