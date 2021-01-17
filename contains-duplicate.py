nums = [2,14,18,22,22]
nums.sort()

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        print(True)
    else:
        print(False)
