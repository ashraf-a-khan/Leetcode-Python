nums = [3,1,3,4,2]

nums.sort()

for i in range(1, len(nums)):
    if nums[i-1] == nums[i]:
        print(nums[i])