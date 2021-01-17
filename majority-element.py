import math
nums = [2, 2, 1, 1, 1, 2, 2]

num_counts = {}

for i in nums:
    if i in num_counts:
        num_counts[i] += 1
    else:
        num_counts[i] = 1

max_ = max(num_counts.values())
major = [k for k,v in num_counts.items() if v == max_]
# print(major[0])
major2 = []

for k, v in num_counts.items():
    if v == max_:
        major2.append(k)

# print(major[0])


count = 0
candidate = None
for num in nums:
    if count == 0:
        # print("Hello")
        candidate = num
    count += (1 if num == candidate else -1)
    print(count)
print(candidate)
