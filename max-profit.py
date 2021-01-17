prices = [7, 1, 5, 3, 6, 4]

min_ = []
max_ = []

for i in range(1, len(prices)):
    min_.append(prices[i])
    max_.append(prices[i] - min(min_))

print(max(max_))

