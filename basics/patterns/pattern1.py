class Solution:
    def pattern1(self,N):
        for i in range(N):
            for i in range(N):
                print("*", end=" ")
            print()
sol=Solution()
N=5
sol.pattern1(N)            