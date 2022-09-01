import sys

a = int(input())
b = list(map(int, sys.stdin.readline().split()))

c = int(input())
d = list(map(int, sys.stdin.readline().split()))

b.sort()

_dict = {}
for i in range(len(b)):
    _dict[b[i]] = 0

for j in range(c):
    if d[j] not in _dict:
        print(0, end=' ')
    
    else:
        print(1, end=' ')
