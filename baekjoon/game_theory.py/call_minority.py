import math

def isMinority(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):  return False
    return True

def get_value(n, m, value_list):
    for j in range(n, m + 1): 
        if isMinority(j):  value_list.append(j)

a, b = map(int, input().split())
c, d = map(int, input().split())

check_list_yt, check_list_yj = [], []
get_value(a, b, check_list_yt)
get_value(c, d, check_list_yj)

merge_list = []
for i in check_list_yt: merge_list.append(i)
for j in check_list_yj: merge_list.append(j)

"""
    The Way No.B-1
"""
set_merge_list = set(merge_list)
print("yj" if len(check_list_yt) == len(check_list_yj) and len(set_merge_list) % 2 == 0 else "yj" if len(check_list_yt) < len(check_list_yj) else "yt")

"""
    The Way No.B-2
"""
# if len(check_list_yt) == len(check_list_yj):
#     set_merge_list = set(merge_list)
#     print('yj' if len(set_merge_list) % 2 == 0 else "yt")
# elif len(check_list_yt) > len(check_list_yj):
#     print('yt')
# elif len(check_list_yt) < len(check_list_yj):
#     print('yj')
