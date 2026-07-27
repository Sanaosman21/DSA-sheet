def pattern18(n):
    for i in range(n):
        start=ord('A')+n-1-i
        for  ch in range(start,ord('A')+n):
            print(chr(ch),end=" ")
        print()
pattern18(5)