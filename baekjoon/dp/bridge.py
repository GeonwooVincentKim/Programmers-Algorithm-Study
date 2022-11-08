import math

a = int(input())

for i in range(a):
    get_value = list(map(int, input().split()))
    print(math.comb(get_value[1], get_value[0]))
