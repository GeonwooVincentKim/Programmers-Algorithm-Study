import sys

n, m = map(int, input().split())

n_set = set()
for i in range(n):
    n_set.add(input())

m_set = set()
for i in range(m):
    m_set.add(input())

intersection_list = list(n_set.intersection(m_set))
intersection_list.sort()

print(len(intersection_list))
for name in intersection_list:
    print(name)
