n = 9
x = y = 0
max_value = -1

mylist = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mylist[i][j] > max_value:
            max_value = mylist[i][j]
            x = i + 1
            y = j + 1

print(max_value)
print(x, y)
