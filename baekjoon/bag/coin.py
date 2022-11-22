import sys

t = int(input())
for i in range(t):
    n = int(input())
    coin_list = list(map(int, sys.stdin.readline().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]
    dp[0] = 1

    for coin in coin_list:
        for j in range(coin, m + 1):
            if j >= coin:
                dp[j] += dp[j - coin]

    print(dp[m])
