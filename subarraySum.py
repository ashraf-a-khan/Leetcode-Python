nums = [1,1,1]
k = 2


count = 0

for start in range(len(nums)):
    for end in range(start+1, len(nums)+1):

        sum1 = 0
        for i in range(start, end):
            sum1 += nums[i]
        if sum1 == k:
            count += 1



print(count)
