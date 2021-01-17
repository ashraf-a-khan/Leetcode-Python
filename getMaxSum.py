arr = [2, 1, 5, 1, 3, 2]
k = 3

arr2 = []
res = 0
for i in range(k):
    res += arr[i]

curr_sum = res
for i in range(k, len(arr)):
    curr_sum += arr[i] - arr[i - k]
    res = max(res, curr_sum)
    