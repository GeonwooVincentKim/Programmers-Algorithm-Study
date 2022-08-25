a, b = map(int, input().split())

sum = 0
for i in range(a + 1, b):
    sum += i

print(sum)
