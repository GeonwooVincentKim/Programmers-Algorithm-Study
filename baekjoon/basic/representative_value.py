list = []
average = 0

for i in range(1, 6):
    a = int(input())
    average += a
    list.append(a)

print(average // 5)
list.sort()

median = 0
idx = 0

if (len(list) % 2 == 0):
    idx = len(list) // 2
    median = (list[idx - 1] + list[idx] / 2)
else:
    idx = len(list) // 2
    median = list[idx]

print(median)
