nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

new_arr = []

for i in nums:
    if i != val:
        new_arr.append(i)

print(len(new_arr))
