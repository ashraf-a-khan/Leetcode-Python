s = '{()}'

p=0

h_map = {}
h_map['('] = ')'
h_map['{'] = '}'
h_map['['] = ']'

stack = []

#print(h_map.keys())

for i in s:
    ch = ""
    if i in h_map.keys():
        stack.append(i)
    elif stack and h_map[stack[-1]] == i:
        stack.pop()
    else:
        print(False)
print(not stack)