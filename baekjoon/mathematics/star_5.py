a = int(input())

for i in range(a + 1):
    for j in range(a - i):
        print(' ', end="")

    for j in range(1, i * 2, 1):
        print('*', end="")
    
    print('')
