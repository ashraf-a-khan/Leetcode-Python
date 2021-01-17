arr = [1,5,11,7]
k = 10
ans = []

for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
            ans.append([arr[i], arr[j]])

print(ans)

