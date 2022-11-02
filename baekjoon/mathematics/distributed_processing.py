a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    n = n % 10

    if n == 0:
        print(10)
    elif n == 1 or n == 5 or n == 6:
        print(n)
    
    elif n == 4 or n == 9:
        m %= 2

        if m == 1:
            print(n)
        else:
            print((n * n) % 10)
    
    else:
        m %= 4
        if m == 0:
            print((n ** 4) % 10 % 10 % 10)
        else:
            print((n ** m) % 10 % 10 % 10)

    