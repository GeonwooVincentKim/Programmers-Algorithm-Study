a = int(input())

outer_list = []
for i in range(a):
    inner_list = list(map(int, input().split()))
    outer_list.append(inner_list)


    