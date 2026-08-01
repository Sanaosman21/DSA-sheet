# n=82
# digit=n%10 #2
# n=n//10  #
# digit2 =n%10 #8
# n=n//10
# print(digit)
# print(digit2)
# print(n)
def sum_of_sq_digit(n):
    total=0
    while(n>0): 
      digit=n%10
      s=digit*digit
      total=total+s
      n=n//10
    return total
def isHappy(n):
   seen=set()
   while(n!=1):
      if n in seen:
         return False
      else:
         seen.add(n)
      n=sum_of_sq_digit(n)
   return True
print(isHappy(19))
print(isHappy(2))