A = [1, 2, 2, 3]

i=0
length = len(A)
while(i < length-1):
    if A[i+1] >= A[i]:
        print(True)
    i += 1

while(i < length-1):
    if A[i+1] <= A[i]:
        print(True)
    i += 1

print(False)