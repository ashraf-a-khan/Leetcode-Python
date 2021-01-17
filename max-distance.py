arrays = [[1,4], [0,5]]

n = len(arrays)
min_val = arrays[0][0]
max_val = arrays[0][-1]
res = 0

for i in range(1, n):
    res = max(res, abs(max_val - arrays[i][0]), abs(arrays[i][-1] - min_val))
    min_val = min(min_val, arrays[i][0])
    max_val = max(max_val, arrays[i][-1])

print(res)