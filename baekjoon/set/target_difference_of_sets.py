import sys

a, b = map(int, input().split())
get_list_a = list(map(int, sys.stdin.readline().split()))
get_list_b = list(map(int, sys.stdin.readline().split()))

set_a = set(get_list_a)
set_b = set(get_list_b)

print(len(set_a ^ set_b))
