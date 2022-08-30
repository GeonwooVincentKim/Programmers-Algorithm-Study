def fibonacci(n):
    dp = [0] * 1000
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


a = int(input())
k = fibonacci(a)
print(k)