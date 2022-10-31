from re import L
import sys
from collections import deque

a = int(input())
# queue_list = []
queue_list = deque([])

for i in range(a):
    liner = sys.stdin.readline().split()
    order = liner[0]
    
    if (order == 'push_back'):
        queue_list.append(liner[1])

    elif (order == 'push_front'):
        queue_list.appendleft(liner[1])
    
    elif (order == 'front'):
        if (queue_list[0] == ''):
            print(-1)
        else:
            print(queue_list[0])
    
    elif (order == 'back'):
        if (queue_list[len(queue_list) - 1] == ''):
            print(-1)
        else:
            print(queue_list[len(queue_list) - 1])
    
    elif (order == 'pop_front'):
        if (len(queue_list) == 0):
            print(-1)
        else:   
            print(queue_list.popleft())
    
    elif (order == 'pop_back'):
        if (len(queue_list) == 0):
            print(-1)
        else:
            print(queue_list.pop())
    
    elif (order == 'size'):
        print(len(queue_list))

    elif (order == 'empty'):
        if (len(queue_list) == 0):
            print(1)
        else:
            print(0)
