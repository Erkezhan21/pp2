def has_33(nums):
    for i in range(0, len(nums)-1):
        if(nums[i] == 3 and nums[i+1] == nums[i]):
            return True
    return False

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

nums = list(map(int, input().split()))
print( has_33(nums) )