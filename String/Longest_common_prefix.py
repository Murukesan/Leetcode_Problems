def longest_common_prefix(strs):
    res=""
    len_list=[]

    for str in strs:
        len_list.append(len(str))
    max_iter = min(len_list)
    for i in range(0, max_iter, 1):
        equal_check=True
        curr_letter=""
        for str in strs:
            if curr_letter=="":
                curr_letter=str[i]
            if str[i]!=curr_letter:
                equal_check=False
                break
        if equal_check==False:
            break
        else:
            res=res+curr_letter
            curr_letter=""

    return res

if __name__=="__main__":
    # Output ---   fl
    strs = ["flower", "flow", "flight"]
    result=longest_common_prefix(strs)
    print(result)
