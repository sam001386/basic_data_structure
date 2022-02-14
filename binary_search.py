
## 找到最左
def bin_left(nums, target):
    left, right = 0, len(nums)-1 
    while left < right:
        mid = (left + right) >> 1 
        if nums[mid] >= target:
            right = mid 
        else:
            left = mid + 1 
    return left

## 找到最优
def bin_right(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right + 1) >> 1 
        if nums[mid] <= target:
            left = mid 
        else:
            right = mid - 1 
    return left 
