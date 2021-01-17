s = "pwwkew"
start = 0
end = 0

max_num = 0
hash_set = set()

while end < len(s):
    if s[end] not in hash_set:
        hash_set.add(s[end])
        end += 1
        max_num = max(len(hash_set), max_num)
    else:
        hash_set.remove(s[start])
        start+=1

print(max_num)
