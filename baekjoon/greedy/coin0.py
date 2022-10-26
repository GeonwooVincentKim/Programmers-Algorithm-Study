a, b = map(int, input().split())
count = 0

list = []
for i in range(a):
    c = int(input())
    list.append(c)

list.sort(reverse=True)

for coin in list:
    count += b // coin
    b %= coin

print(count)
