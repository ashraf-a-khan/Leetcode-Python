nums = [1, 2, 3, 4, 5, 6, 7]

k = 3
nums2 = []

nums[:] = nums[len(nums)-k:]+nums[0:len(nums)-k]