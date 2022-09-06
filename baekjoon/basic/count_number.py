a = int(input())
b = list(map(int, input().split()))
c = int(input())

count = 0

for i in b:
    count = b.count(c)
print(count)
