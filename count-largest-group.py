n=57

d = {}
cnt = 0
for i in range(1, n+1):
    if i > 9:
        i = sum([int(j) for j in str(i)])
        print(i)
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
max_cnt = max(d.values())
for c in d.values():
    if c == max_cnt:
        cnt += 1
print("  " +str(cnt))
