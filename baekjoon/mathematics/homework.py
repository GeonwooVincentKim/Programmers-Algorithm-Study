total = []
for i in range(1, 7):
    total.append(i)

value = []
for i in range(6):
    a = int(input())
    value.append(a)

for i in total:
    if i not in value:
        print("Print -> {0}".format(i))
