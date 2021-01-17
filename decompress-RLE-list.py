nums = [1, 2, 3, 4]

if len(nums) % 2 != 0:
    print(-1)

my_list = []
for i in range(0,len(nums),2):
    freq = nums[i]
    value = nums[i+1]
    for i in range(freq):
        my_list.append(value)

print(my_list)