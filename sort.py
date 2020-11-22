# Quick sort
def sortArray(self, nums):
    def quick_sort(nums, l, r):
        if l >= r:
            return 
        i = l - 1 
        j = r + 1 
        x = nums[(l + r) // 2]
        while i < j:
            i += 1 
            while nums[i] < x:
                i += 1 
            j -= 1 
            while nums[j] > x:
                j -= 1 
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        quick_sort(nums, l, j)
        quick_sort(nums, j + 1, r)

    quick_sort(nums, 0, len(nums) - 1)
    return nums
