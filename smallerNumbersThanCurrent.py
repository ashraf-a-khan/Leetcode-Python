nums = [8,1,2,2,3]
temp = sorted(nums)
map = {}


for i in range(len(temp)):
    if temp[i] not in map:
        map[temp[i]] = i
    else:
        i += 1

print([map[x] for x in nums])