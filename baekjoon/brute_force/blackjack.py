a, b = map(int, input().split())
value = list(map(int, input().split()))

sum = 0
index_total = 0

for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a):
            index_total = value[i] + value[j] + value[k]

            if (index_total > b):
                continue
            else:
                sum = max(sum, index_total)

print(sum)
