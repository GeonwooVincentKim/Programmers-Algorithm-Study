import sys

a = int(sys.stdin.readline())
dp = [0] * 10001

for i in range(a):
    dp[int(sys.stdin.readline())] += 1

for i in range(10001):
    if dp[i] != 0:
        for j in range(dp[i]):
            print(i)
