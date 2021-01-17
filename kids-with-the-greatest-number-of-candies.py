candies = [2, 3, 5, 1, 3]
extraCandies = 3
max_candy = max(candies)
solution = []
for candy in candies:
    if candy + extraCandies >= max_candy:
        solution.append(True)
    else:
        solution.append(False)

print(solution)
