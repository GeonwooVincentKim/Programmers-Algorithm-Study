a, b, c = map(int, input().split())

max_value = []
sum = 0
total = 0

if a == b == c:
    sum = 10000 + a * 1000
    print(sum)

elif a == b:
    sum = 1000 + a * 100
    print(sum)
    
elif b == c:
    sum = 1000 + b * 100
    print(sum)

elif a == c:
    sum = 1000 + a * 100
    print(sum)

else:
    sum = 100 * max(a, b, c)
    print(sum)
