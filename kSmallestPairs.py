import heapq

nums1 = [1, 7, 11]
nums2 = [1, 4, 6]
k = 3

pairs = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        pairs.append((nums1[i], nums2[j]))

print(pairs)
pairs.sort(key = lambda x: x[0] + x[1])
# heapq.heapify(pairs)
print(pairs)

result = []
for i in range(k):
    result.append((pairs[i][0], pairs[i][1]))

print(result)