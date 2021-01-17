#The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
#Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
#Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

people = [3,2,2,1]
limit = 3

left = 0
right = len(people) - 1
people.sort()
boat = 0

while left <= right:
    if left == right:
        boat += 1
        break;
    elif people[left] + people[right] <= limit:
        left += 1
        right -= 1
        boat += 1
    elif people[left] + people[right] > limit:
        right -= 1
        boat += 1

print(boat)


