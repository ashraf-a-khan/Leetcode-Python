s = "the sky is blue"
t = s.split()
arr = []
ans = " "
for i in reversed(t):
    arr.append(i)

print(ans.join(arr))