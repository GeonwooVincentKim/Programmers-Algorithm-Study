def fibonacci(n):
    x, y = 0, 1

    for _ in range(n):
        x, y = y, x + y
    return x


print(fibonacci(int(input())))
