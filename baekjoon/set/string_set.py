import sys

n, m = map(int, input().split())
count = 0

string_set = {sys.stdin.readline().replace("\n", "") for _ in range(n)}

for j in range(m):
    if sys.stdin.readline().replace("\n", "") in string_set : count += 1
print(count)
