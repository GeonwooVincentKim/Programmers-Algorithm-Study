a = int(input())
b = int(input())

sum = 0
minority = []

for i in range(a, b + 1):
    result = True

    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                result = False
                break
        
        if(result):
            minority.append(i)
            sum = sum + i

if len(minority) > 0:
    print(sum)
    print(min(minority))
else:
    print(-1)
