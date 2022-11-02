if __name__ == "__main__":
    a = int(input())

    stack_list = []
    for i in range(a):
        k = int(input())

        if k == 0:
            stack_list.pop()
        else:
            stack_list.append(k)

    sum = 0
    for i in range(len(stack_list)):
        sum += stack_list[i]

    if len(stack_list) == 0:
        print(0)
    else:
        print(sum)