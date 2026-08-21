from collections import deque

def fun(nums, k):
    q = deque()
    l = 0
    r = 0
    while r < len(nums):
        if nums[r] < 0:
            q.append((nums[r], r))
        if r - l + 1 == k:
            while q and q[0][1] < l:
                q.popleft()
            if q:
              print(q[0][0])
            else:
                print(0)
            l += 1
        r += 1
nums = [12, -1, -7, 8, -15, 30, 16, 28]
print(fun(nums,3))
