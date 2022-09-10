total = []
for i in range(1, 31):
    total.append(i)

value = []
for i in range(28):
    a = int(input())
    value.append(a)

for i in total:
    if i not in value:
        print(i)
