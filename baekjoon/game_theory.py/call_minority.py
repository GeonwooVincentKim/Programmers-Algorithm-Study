import math


def isMinority(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True


def get_value(n, m, value_list):
    for j in range(n, m + 1):
        if isMinority(j):
            value_list.append(j)


a, b = map(int, input().split())
c, d = map(int, input().split())

check_list = []

get_value(a, b, check_list)
get_value(c, d, check_list)

set_list = set(check_list)

if len(set_list) % 2 == 0:
    print('yj')
else:
    print('yt')
