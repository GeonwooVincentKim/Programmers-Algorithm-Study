import sys

m = int(input())
p = list(map(int, sys.stdin.readline().split()))

value = 0
for i in p:
    value ^= i

print("koosaga" if (value != 0) else "cubelover")
