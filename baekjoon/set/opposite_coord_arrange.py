a = int(input())

b_list = []

for i in range(a):
    b_list.append(list(map(int, input().split())))

b_list.sort(key=lambda x: (x[1], x[0]))

for i in b_list:
    print(i[0], i[1])
