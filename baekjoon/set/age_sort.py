a = int(input())

b_list = []
for i in range(a):
    b, c = map(str, input().split())
    b = int(b)
    b_list.append((b, c))

b_list.sort(key=lambda x: x[0])

for i in b_list:
    print(i[0], i[1])

