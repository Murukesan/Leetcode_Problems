def Rotate_array(nums,k):
    n = len(nums)
    k = k % n  # handle case when k > n
    nums[:] = nums[-k:] + nums[:-k]  # update in place
    return nums
if __name__=='__main__':
    nums=[1,2,3,4,5,6,7]
    res=Rotate_array(nums,3)
    print(res)