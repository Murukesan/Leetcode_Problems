def Third_Maximum(nums):
    lst = list(set(nums))
    if len(lst) > 3 or len(lst) == 3:
        lst.sort(reverse=True)
        return lst[2]
    else:
        return max(lst)

if __name__=='__main__':
    nums=[1,1,2,2,3,5]
    res=Third_Maximum(nums)
    print(res)