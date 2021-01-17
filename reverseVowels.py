#Convert the string to list
#Declare 2 lists and push each element individually in those stacks
#Now reverse the vowel list obtained
#In new list named "res", compare the inital list and push the elements in the res list accordingly.

s = "leetcode"

d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vow = ''
for char in s:
    if char in d:
        vow += char

vow = vow[::-1]
ans = ''
i=0
for char in s:
    if char not in d:
        ans += char
    else:
        ans += vow[i]
        i += 1
print(ans)