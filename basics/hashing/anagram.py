def anagram(str1 , str2):
    dict={}
    if len(str1)!=len(str2):
        return False
    for ch in str1:
        if ch in dict:
            dict[ch]+=1
        else:
            dict[ch]=1
    for ch in str2 :
        if ch not in dict:
            return False
        else:
            dict[ch]-=1
    if dict[ch]<0:
        return False 
    return True 
print(anagram("listen","silent"))
print(anagram("abc","abd"))
print(anagram("aab","abb"))