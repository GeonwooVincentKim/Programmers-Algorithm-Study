import math

a = int(input())

for i in range(a):
    inner_list = list(map(int, input().split()))
    print(math.comb(inner_list[0], inner_list[1]))
