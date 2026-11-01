n = int(input("Enter no of items: "))

weights = []
profits = []

for i in range(n):
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = int(input("Enter capacity: "))

# Create DP table
dp = []

for i in range(n + 1):
    dp.append([0] * (capacity + 1))

# Fill DP table
for i in range(1, n + 1):
    for j in range(1, capacity + 1):

        if weights[i - 1] <= j:
            dp[i][j] = max(
                profits[i - 1] + dp[i - 1][j - weights[i - 1]],
                dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print("Maximum Profit:", dp[n][capacity])