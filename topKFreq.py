nums = [1,1,1,2,2,3]
k = 2

h_map = {}

for num in nums:
    if num in h_map:
        h_map[num] += 1
    else:
        h_map[num] = 1

print(h_map)
ans = []
for key, val in h_map.items():
    if val >= k:
        ans.append(key)

print(ans)
