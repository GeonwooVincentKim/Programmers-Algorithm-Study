from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())

# list = []
# for i in range(1, n + 1):
#     list.append(i)

#     if (i % 2 == 1):
#         list.remove(list[0])
#     # elif (list[0] % 2 == 0):
#         # list.insert(n - 1, list[0])
#         # list.remove(list[0])
#         # list.remove(i)

#     elif (i % 2 == 0):
#         list.insert(n - 1, list[0])
#         list.remove(list[0])
# print(list)


"""
1. N = 6
list = [1, 2, 3, 4, 5, 6]

2. Remove first odd value from the list
list = [2, 3, 4, 5, 6]

3. Move first even value to the last area of the list
list = [3, 4, 5, 6, 2]

4. Remove first odd value from the list
list = [4, 5, 6, 2]

5. Move first even value to the last area of the list
list = [5, 6, 4]

6. Remove first odd value from the list
list = [6, 4]

7. Remove first value from the list (2 value remain)
list = [4]
"""