def pattern14(n):
    for i in range(1,n+1):
        for j in range(ord('A'),ord('A')+i):
            print(chr(j),end=" ")
        print()
pattern14(8)
# //  for j in range(ord('A'),ord('A')+n-i+1): to reciprpcal a pattern