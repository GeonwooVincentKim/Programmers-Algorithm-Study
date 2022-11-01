from collections import deque

a, b = map(int, input().split())
queue = deque([])
answer = []

for i in range(1, a + 1):
    queue.append(i)

while queue:
    for i in range(b - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end="")
for i in range(len(answer) - 1):
    print("{0}, ".format(answer[i]), end="")

print(answer[-1], end="")
print(">")

"""
1. Save into Queue
2. Print < and >
3. Pop the value which are already stored in the Queue
"""