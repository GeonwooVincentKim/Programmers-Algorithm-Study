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

# check_list = []
check_list_yt = []
check_list_yj = []

get_value(a, b, check_list_yt)
get_value(c, d, check_list_yj)

# get_value(c, d, check_list_yj)
print("check_list Yoontae -> {0}".format(check_list_yt))
print("check_list Yujin -> {0}".format(check_list_yj))


# set_list_yt = set(check_list_yt)
# set_list_yj = set(check_list_yj)
# sorted(set_list_yj)

# print("set_list_yt -> {0}".format(set_list_yt))
# print("set_list_yj -> {0}".format(set_list_yj))
# if len(set_list_yt) == len(set_list_yj):


# if len(set_list) % 2 == 0:
#     print('yj')
# elif a == 2 and b == 3 and c == 5 and d == 11:
#     print('yj')
# else:
#     print('yt')
