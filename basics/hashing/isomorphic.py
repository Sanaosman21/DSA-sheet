s="paper"
t="title"
def fun(s,t):
    map={}
    used=set()
    for i in range(len(s)):
        if s[i] in map:
            if map[s[i]]!=t[i]:
                return False
            else:
                continue
        else:
            if t[i] in used:
                return False
            else:
                map[s[i]]=t[i]
                used.add(t[i])
    return True
print(fun("paper","title"))
print(fun("abb","aab"))