def fun(n):
    if n==0:
        return 0
    return fun(n-1)+fun(n-2)
print(fun(4))