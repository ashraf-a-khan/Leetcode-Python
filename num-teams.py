rating = [2, 5, 3, 4, 1]
ans = []
n = len(rating)
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if rating[i] < rating[j]:
                if rating[j] < rating[k]:
                    ans.append([rating[i], rating[j], rating[k]])
            if rating[i] > rating[j]:
                if rating[j] > rating[k]:
                    ans.append([rating[i], rating[j], rating[k]])

print(ans)
