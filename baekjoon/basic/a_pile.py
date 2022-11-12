import sys

t = int(sys.stdin.readline())

for i in range(t):
    odd = 0
    even = 0

    list_value = list(map(int, sys.stdin.readline().split()))

    for i in range(3):
        if list_value[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if (even == 3 or even == 2):
        print('R')
    else:
        print('B')
