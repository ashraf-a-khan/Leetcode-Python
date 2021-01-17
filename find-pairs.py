nums = [1, 3, 1, 5, 4]
k = 0
my_list = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if abs(nums[i] - nums[j]) == k:
            my_list.append([nums[i], nums[j]])

print(my_list)

ans = (set(tuple(i) for i in my_list))

print(len(ans))


