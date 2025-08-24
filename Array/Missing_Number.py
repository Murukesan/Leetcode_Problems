def Missing_Number(nums):
    for i in range(0,len(nums),1):
        if i not in nums:
            return i
    return len(nums)+1
if __name__=='__main__':
    nums=[9,6,4,2,3,5,7,0,1]
    res=Missing_Number(nums)
    print(res)