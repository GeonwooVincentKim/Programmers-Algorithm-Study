n, m = map(int, input().split())

array = []

def backtracker_array(start):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return

    for i in range(start, n + 1):
        if i not in array:
            array.append(i)
            backtracker_array(i + 1)
            array.pop()


backtracker_array(1)
