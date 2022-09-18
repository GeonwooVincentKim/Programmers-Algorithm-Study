import sys

a = int(input())

stack_list = []

for i in range(a):
    value = sys.stdin.readline().split()
    order = value[0]
    
    if (order == 'push'):
        stack_list.append(value[1])
    
    elif (order == 'top'):
        if (len(stack_list) == 0):
            print(-1)
        else:
            print(stack_list[-1])
    
    elif (order == 'pop'):
        if (len(stack_list) == 0):
            print(-1)
        else:
            print(stack_list.pop())
    
    elif (order == 'size'):
        print(len(stack_list))
    
    elif (order == 'empty'):
        if (len(stack_list) == 0):
            print(1)
        else:
            print(0)
