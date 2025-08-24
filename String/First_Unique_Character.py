def First_Unique_Char(s):
    frequency={}
    for i in range(len(s)):
        if s[i] in frequency:
            frequency[s[i]]+=1
        else:
            frequency[s[i]]=1
    for i in range(len(s)):
        if frequency[s[i]]==1:
            return i
    return -1
if __name__=="__main__":
    str="leetcode"
    res=First_Unique_Char(str)
    print(res)