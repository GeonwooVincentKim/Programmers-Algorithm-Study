import sys
import math

n = int(sys.stdin.readline())

division_num = 0

get_aliquot_list = []
for i in range(2, round(float(n + 1))):
    if n % i == 0:
        division_num += 1
        if (division_num > 1):
            break

        n /= i
        i -= 1


if division_num == 1:
    print("cubelover")
else:
    print("koosaga")

# print(get_aliquot_list)


