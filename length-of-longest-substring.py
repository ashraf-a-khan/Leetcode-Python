s = "pwwkew"

ans = []
count = 0
for i in s:
    if i not in ans:
        ans.append(i)
        count = max([count, len(ans)])
        print(ans)
    else:
        # print("*****")
        ans = ans[ans.index(i) + 1:]
        ans.append(i)
        print(ans)

#print(ans)
print(count)
