import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

num_dict = {}
for i in range(len(a)):
    num_dict[a[i]] = i

for i in numbers:
    print(num_dict[i], end=' ')
