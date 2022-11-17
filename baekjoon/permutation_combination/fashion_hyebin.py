import sys
from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())

    clothes_list = [sys.stdin.readline().split() for _ in range(n)]
    value_list = []

    for j in clothes_list:
        value_list.append(j[1])

    counter = Counter(value_list)
    count_value = 1

    for k in counter:
        count_value *= counter[k] + 1

    print(count_value - 1)
    # for j in clothes_list:
    #     get_list = clothes_list[j].split()
    #     print(get_list)

    # for j in range(n):
    # for j in range(n):
    #     sort, kind = sys.stdin.readline().split()
