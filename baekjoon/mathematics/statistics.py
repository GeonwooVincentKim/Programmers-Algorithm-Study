from collections import Counter
import sys

a = int(input())

get_value = []

for i in range(a):
    get_value.append(int(sys.stdin.readline()))

print(round(sum(get_value) / len(get_value)))

centerIndex = len(get_value) // 2
get_value.sort()
print(get_value[centerIndex])

c = Counter(get_value).most_common()
maximum = c[0][1]

## Print Mode
modes = []
for num in c:
    if num[1] == maximum:
        modes.append(num)

## Sort Mode
if len(modes) != 1:
    modes = sorted(modes)
    print(modes[1][0])
else:
    print(modes[0][0])

print(max(get_value) - min(get_value))
