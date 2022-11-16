import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))


def grundy(n):
    return (n + 1) // 2 if n % 2 == 1 else (n - 2) // 2

value = 0
for i in p:
    value ^= grundy(i)

print("koosaga" if value > 0 else "cubelover")
