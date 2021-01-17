A = [3,1,2,4]

evenArr = []
oddArr = []

for a in A:
    if a%2 == 0:
        evenArr.append(a)
    else:
        oddArr.append(a)

final_list = evenArr+oddArr

print(final_list)
