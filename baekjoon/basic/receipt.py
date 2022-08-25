a = int(input())
b = int(input())

innerSum = 0
storeSum = []

for i in range(1, b + 1):
    c, d = map(int, input().split())
    innerSum = c * d
    storeSum.append(innerSum)

if ((sum(storeSum)) == a):
    print("Yes")
else:
    print("No")
