n, k = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

dp = [0] + [100001 for _ in range(k)]

for i in coin_list:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] = min(dp[j - i] + 1, dp[j])

if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)
