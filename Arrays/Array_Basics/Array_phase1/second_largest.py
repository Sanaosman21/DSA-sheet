# class Solution:
def fun(arr):
        largest=arr[0]
        second_largest=float('-inf')
        for i in arr[1:]:
            if i>largest:
                second_largest=largest
                largest=i
            if i<largest and i>second_largest:
                 second_largest=i
        return second_largest
# arr = [4, 7, 2, 9, 8]
arr = [-5, -2, -8]
print(fun(arr))
# sol=Solution()
# arr=[4, 7, 2, 9, 5]
# sol.fun(arr)
