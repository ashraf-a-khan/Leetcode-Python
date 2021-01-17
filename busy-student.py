startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

left = 0
right = len(startTime)

counter = 0

while left < right:
    if endTime[left] >= queryTime >= startTime[left]:
        counter += 1

    left += 1

print(counter)


