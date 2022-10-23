while True:
    a = input()
    cnt = 0

    for string in a:
        if string in 'aeiouAEIOU':
            cnt += 1

    if (a == '#'):
        break

    print(cnt)
