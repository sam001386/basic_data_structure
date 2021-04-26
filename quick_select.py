def quicksort(l, r, k, nums):
    if l >= r:
        return nums[l]
    pivot = nums[(l + r) >> 1]
    i, j = l - 1, r + 1
    while i < j:
        while True:
            i += 1 
            if pivot <= nums[i]:
                break
        while True:
            j -= 1 
            if pivot >= nums[j]:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    #make sure the kth smallest number is in the recursion
    if j < k - 1:
        quicksort(j + 1, r, k, nums)
    else:
        quicksort(l, j, k, nums)

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    nums = map(int, raw_input().split())
    quicksort(0, n - 1, k, nums)
    print(nums[k - 1])
