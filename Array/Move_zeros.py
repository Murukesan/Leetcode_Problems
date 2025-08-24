def Move_zeros(nums):
    size=len(nums)
    for i in range(size):
        if nums[i]==0:
            for j in range(i+1,size,1):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
    return nums
if __name__=='__main__':
    res=Move_zeros([0,1,0,3,12])
    print(res)