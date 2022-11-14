import sys
import math

n = int(sys.stdin.readline())

get_aliquot_list = []

count = 0
while n and count <= 2:
    flag = False

    for i in range(2, n):
        if (not (n % i)):
            count += 1
            n /= i
            flag = True
            break
    
    if n == 1:  break
    elif (not flag):    
        count += 1  
        break

if (count == 0 or count == 1 or count == 3):
    print("koosaga")
else:
    print("cubelover")


# for i in range(2, i * i):
#     if n % i == 0:
#         division_num += 1
#         if (division_num > 1):
#             break

        # n /= i
        # i -= 1


# if division_num == 1:
#     print("cubelover")
# else:
#     print("koosaga")

# print(get_aliquot_list)
