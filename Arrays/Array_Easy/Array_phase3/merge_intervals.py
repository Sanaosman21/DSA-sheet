# Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
#brute force 
def fun(intervals):
    intervals.sort()
    ans=[]
    n=len(intervals)
    i=0
    while(i<n):
        start=intervals[i][0]
        end=intervals[i][1]
        j=i+1
        while j<n and intervals[j][0]<=end:
            end=max(end,intervals[j][1])
            j=j+1
        ans.append([start,end])
        i=j
    return ans
intervals=[[1,3],[2,6],[8,10],[9,11]]
print(fun(intervals))

#optimal appraoch
def merge(intervals):
    result=[]
    intervals.sort()
    for interval in intervals :
        if not result :
            result.append(interval)
        elif result[-1][1]>=interval[0]:
            result[-1][1]=max(result[-1][1],interval[1])
        else:
            result.append(interval)
    return result
intervals=[[1,3],[2,6],[8,10],[9,11]]
print(merge(intervals))

# 1. Intervals are unordered
#         ↓
#    Sort by START

# 2. Take intervals one by one
#         ↓
# 3. Look only at the LAST interval in result
#         ↓
# 4. Compare:
#    last_end  vs  current_start
#         ↓
# 5. If they overlap
#         ↓
#    Extend the END
#         ↓
# 6. If they don't overlap
#         ↓
#    Start a NEW interval
            
