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
- 1. Iterate deque_list and append into josephus_list which shows the result of josephus-permutation
- 2. If the number is multiples of K (In this case, it's 3), Add into Josephus_list and delete from deque_list
  = 1. Move the selected number to the
- 3. If it space 3 place from previous number, Add into Josephus_list and delete from deque_list
"""