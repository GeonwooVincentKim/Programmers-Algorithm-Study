a, b = map(int, input().split())

array = []


def backtracker_array(k, n, m):
    if k == m:
        print(' '.join(map(str, array)))
        return

    for i in range(1, n + 1):
        array.append(i)
        backtracker_array(k + 1, n, m)
        array.pop()


backtracker_array(0, a, b)

