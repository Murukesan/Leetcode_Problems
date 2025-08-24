def Single_Number(nums):
    if len(nums)==1:
        return nums[0]
    else:
        lst = []
        seen = []
        for i in nums:
            if i not in lst and i not in seen:
                lst.append(i)
            else:
                lst.remove(i)
                seen.append(i)
        return lst
if __name__=="__main__":
    nums=[4, 1, 2, 1, 2]
    res=Single_Number(nums)
    print(res)