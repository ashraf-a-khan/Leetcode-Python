arr = [1, 2, 2, 3, 3, 3]

ans = set()

for i in arr:
    if arr.count(i) == i:
        ans.add(i)

print(ans)
print(max(ans))

h_map = {}
for i in arr:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1

print(h_map)
ans2 = []
for k, v in h_map.items():
    if v == k:
        ans2.append(k)

print(max(ans2))