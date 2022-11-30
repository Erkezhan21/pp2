def spy_game(nums):
    for i in range(0, len(nums)-2):
        for j in range(0, len(nums)-2):
            if(nums[i] == 0 and nums[j] == 0 and nums[i+2] == 7):
                return True
    return False

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

nums = list(map(int, input().split()))
print(spy_game(nums) )