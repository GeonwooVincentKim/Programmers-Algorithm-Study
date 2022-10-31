def solution(a, b):
    n = len(a)
    multi_array = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                multi_array[i][j] += a[i][k] * b[k][j]

    return multi_array


if __name__ == "__main__":
    a_list_col, a_list_row = map(int, input().split())

    a_list = []
    for i in range(a_list_col):
        a_list.append(list(map(int, input().split())))

    b_list_col, b_list_row = map(int, input().split())

    b_list = []
    for i in range(b_list_col):
        b_list.append(list(map(int, input().split())))

    answer = solution(a_list, b_list)
    print(answer)
    # a = list(map(int, input().split()))
    # b = list(map(int, map(int, input().split())))
    # print(a, b)
