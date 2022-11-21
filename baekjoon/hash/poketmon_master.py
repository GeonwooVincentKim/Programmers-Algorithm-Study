import sys

poketmon_dict = {}
n, m = map(int, input().split())

for i in range(1, n + 1):
    inner = sys.stdin.readline().rstrip()
    poketmon_dict[i] = inner
    poketmon_dict[inner] = i

for j in range(m):
    inner_question = sys.stdin.readline().rstrip()

    if inner_question.isdigit():
        print(poketmon_dict[int(inner_question)])
    else:
        print(poketmon_dict[inner_question])
