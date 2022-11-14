import sys

def euclid(a, b):
    if a > b:
        a, b = b, a

    if b % a == 0:
        return True

    if (b - a < a):
        return not euclid(b - a, a)

    return True


while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break

    print("A wins" if euclid(a, b) else "B wins")


