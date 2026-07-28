
def sumParamterised(i,sum):
    if (i<1):
        print(sum)
        return
    sumParamterised(i-1,sum+i)
sumParamterised(5,0)



































