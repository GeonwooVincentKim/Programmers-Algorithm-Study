n, k = map(int, input().split())


if n == 0:
    print("HS" if k % 6 == 1 else "YG")
elif n == 1:
    print("HS" if k % 6 == 0 or k % 6 == 5 else "YG")
