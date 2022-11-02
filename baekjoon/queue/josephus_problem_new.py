from collections import deque

n, k = map(int, input().split())
deque_list = deque([])
josephus_list = []

for i in range(1, n + 1):
    deque_list.append(i)

for i in range(len(deque_list)):
    for j in range(k - 1):
        deque_list.append(deque_list.popleft())
    josephus_list.append(deque_list.popleft())

print(deque_list)
print(josephus_list)

"""
Josephus Problem
1. Add into deque_list
2. Get the recurrence formula
- 1. 
"""