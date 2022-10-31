def solution(a, b):
    n = len(a)
    multi_array = [[0] * len(b[0]) for _ in range(n)]

    for i in range(n):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                multi_array[i][j] += a[i][k] * b[k][j]

    return multi_array


if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
