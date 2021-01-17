J = "aA"
S = "aAAbbbb"
h_map = {}
count = 0

for i in J:
    if i in h_map:
        h_map[i] += 1
    else:
        h_map[i] = 1

for i in S:
    if i in h_map:
        count += 1


print(count)
