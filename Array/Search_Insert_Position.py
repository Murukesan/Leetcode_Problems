def search_insert_position(nums,target):
    start = 0
    end = len(nums) - 1
    mid = 0
    while (start <= end):
        mid = (start + end) // 2
        if (nums[mid] == target):
            return mid
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return start
if __name__=="__main__":
    nums=[1001]
    target=5
    res=search_insert_position(nums,target)
    print(res)