a, b = map(int, input().split())

dp = [0 for _ in range(b + 1)]
dp[0] = 1

coin_list = []
for i in range(a):
    coin_list.append(int(input()))

for coin in coin_list:
    for j in range(coin, b + 1):
        dp[j] += dp[j - coin]

print(dp[b])
