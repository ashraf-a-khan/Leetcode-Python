import heapq

words = [1,1,1,2,2,3]
k = 2

h_map = {}

for i in words:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1

print(h_map)

pairs = []

for num, count in h_map.items():
    pairs.append((-count, num))

print(pairs)

heapq.heapify(pairs)

print(pairs)
result = []
for _ in range(k):
    result.append(heapq.heappop(pairs)[1])

print(result)