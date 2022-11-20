nums = range(2, 100)
for i in range(2, 10):
    nums = list(filter(lambda x: x % i !=0, nums))
print(nums)
