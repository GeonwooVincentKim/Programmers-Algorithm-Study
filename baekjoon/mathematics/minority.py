a = int(input())
b = int(input())

sum = 0
minority = []

for i in range(a, b):
    result = True

    for j in range(2, a):
        if (i % j == 0):
            result = False
    
    if(result):
        minority.append(i)
        sum = sum + i

if len(minority) > 0:
    print(sum)
    print(min(minority))
else:
    print(-1)
