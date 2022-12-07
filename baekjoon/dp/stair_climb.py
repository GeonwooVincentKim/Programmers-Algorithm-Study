import sys
dp = []
array = []

n = int(input())
for i in range(n):
    array.append(int(sys.stdin.readline()))

dp.append(array[0])
dp.append(max(array[0] + array[1], array[1]))
dp.append(max(array[0] + array[2], array[1] + array[2]))

for i in range(3, n):
    dp.append(max(dp[i-2] + array[i] , dp[i-3] + array[i] + array[i - 1]))

print(dp.pop())
