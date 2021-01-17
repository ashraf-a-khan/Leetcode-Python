import sys
arr = [4, 2, 1, 3]

my_list1 = []
my_list2 = []
arr.sort()

for i in range(len(arr)-1):
    # print(arr[i+1]-arr[i])
    my_list2.append(arr[i+1]-arr[i])

minimum = min(my_list2)
for i in range(len(arr)-1):
    diff = abs(arr[i+1]-arr[i])
    if diff == minimum:

        my_list1.append([arr[i+1],arr[i]])

print(my_list1)