import sys

n, m = map(int, input().split())

get_list = []
for i in range(n + m):
    value = input()
    get_list.append(value)

get_duplicate = [x for i, x in enumerate(get_list) if i != get_list.index(x)]
print(len(get_duplicate))

for i in get_duplicate:
    print(i)
