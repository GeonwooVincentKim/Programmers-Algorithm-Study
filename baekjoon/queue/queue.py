import sys

a = int(input())
queue_list = []

for i in range(a):
    value = sys.stdin.readline().split()
    order = value[0]

    if (order == 'push'):
        queue_list.insert(0, value[1])
    
    elif (order == 'pop'):
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
    
    elif (order == 'front'):
        if (len(queue_list) == 0):
            print(-1)
        else:
            print(queue_list[len(queue_list) - 1])

    elif (order == 'back'):
        if (len(queue_list) == 0):
            print(-1)
        else:
            print(queue_list[0])
