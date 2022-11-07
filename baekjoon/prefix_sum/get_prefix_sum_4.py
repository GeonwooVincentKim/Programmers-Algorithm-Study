a, b = map(int, input().split())
get_list = list(map(int, input().split()))

prefix_list = []
for i in range(b):
    value = list(map(int, input().split()))
    prefix_list.append(value)

prefix_sum = [0]
numbers_sum = 0

for number in get_list:
    numbers_sum += number
    prefix_sum.append(numbers_sum)

for i_j in prefix_list:
    i, j = i_j[0], i_j[1]
    print(prefix_sum[j] - prefix_sum[i - 1])
