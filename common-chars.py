my_list = ["bella", "label", "roller"]
h_map = {}

for i in my_list:
    for j in i:
        if j in h_map:
            h_map[j] += 1
        else:
            h_map[j] = 1

length = len(my_list)
print(h_map)
solution = []
for k, v in h_map.items():
    if v%length == 0:
        solution.append(k)

print(solution)

