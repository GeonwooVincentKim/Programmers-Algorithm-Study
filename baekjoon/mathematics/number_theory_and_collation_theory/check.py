n = int(input())

value_list = []
number_difference = 0
value_rest_number = 0

for i in range(n):
    m = int(input())

    if m % n == 0:
        continue
    # if m % i == 0:
    #     continue
    else:
        value_rest_number = m % n

    value_list.append(m)
