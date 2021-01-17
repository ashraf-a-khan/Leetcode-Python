nums = [1, 2, 3, 4, 2, 3, 6, 7, 8, 4]

h_map = {}

for i in nums:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1


for k,v in h_map.items():
    if v > 1:
        print(k)