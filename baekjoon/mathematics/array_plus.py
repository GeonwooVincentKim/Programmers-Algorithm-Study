a, b = map(int, input().split())

outer = []
inner = []

for row in range(a):
    row = list(map(int, input().split()))
    outer.append(row)

for row in range(a):
    row = list(map(int, input().split()))
    inner.append(row)

for row in range(a):
    for col in range(b):
        print(outer[row][col] + inner[row][col], end=' ')
    print()
