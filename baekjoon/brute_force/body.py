n = int(input())

total = []
answer = []

for i in range(n):
    a, b = map(int, input().split())
    total.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if total[i][0] < total[j][0] and total[i][1] < total[j][1]:
            count += 1
        
    answer.append(count + 1)

for i in answer:
    print(i, end=" ")
