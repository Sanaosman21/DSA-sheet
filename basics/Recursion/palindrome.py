def fun(i,str):
    
    if i>=len(str)//2:
        return True
    if str[i]!=str[len(str)-i-1]:
        return False  
    return fun(i+1,str)
print(fun(0,"madam") )
print(fun(0,"abba"))
print(fun(0,"sana"))
print(fun(0,"racecar"))