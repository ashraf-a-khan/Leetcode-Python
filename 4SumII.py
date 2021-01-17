A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]


m = {}
sum1 = []
sum2 = []
count = 0

for i in range(len(A)):
    for j in range(len(B)):
        x = A[i]
        y = B[j]
        sum1.append(x + y)

for i in sum1:
    if i not in m:
        m[i] = 0
    m[i] += 1

print(m)
for i in range(len(C)):
    for j in range(len(D)):
        x = A[i]
        y = B[j]
        target = -(x + y)
        if target in m:
            count += m[target]

print(count)