n = int(input())

list = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            list[i][j] = 1

count = 0
for row in list:
    count += row.count(1)

print(count)
