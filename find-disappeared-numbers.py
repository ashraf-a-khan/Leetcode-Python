nums = [4, 3, 2, 7, 8, 2, 3, 1]
h_map = {}

for i in nums:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1

print(h_map)
ans = []

for i in range(1, len(nums)):
    if i not in h_map.keys():
        ans.append(i)

print(ans)



