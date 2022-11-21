import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))

value = 0
flag = 0

for i in p:
    if i > 1:   flag = 1
    value ^= i

if (flag == 1):    print("cubelover" if not value else "koosaga")
else:   print("cubelover" if n % 2 else "koosaga")
