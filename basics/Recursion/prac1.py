def fun(n):
    if n==0:
        return
    print("before",n)
    fun(n-1)
    print("after",n)
fun(3)