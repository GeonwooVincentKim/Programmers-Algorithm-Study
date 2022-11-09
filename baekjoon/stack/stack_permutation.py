n = int(input())

stack_list = []
stack_list_copy = []
value = 1

checkFindValue = True

for i in range(n):
    inner = int(input())

    while value <= inner:
        stack_list.append(value)
        stack_list_copy.append('+')
        value += 1

    if stack_list[-1] == inner:
        stack_list.pop()
        stack_list_copy.append('-')
    
    else:
        checkFindValue = False

if checkFindValue == False:
    print('NO')

else:
    for i in stack_list_copy:
        print(i)
