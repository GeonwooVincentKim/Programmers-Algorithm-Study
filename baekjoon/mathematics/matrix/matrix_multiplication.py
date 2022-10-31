def solution(N, M, a_list, K, b_list):
    multi_array = [[0] * K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for k in range(M):
                multi_array[i][j] += a_list[i][k] * b_list[k][j]
    return multi_array


if __name__ == "__main__":
    N, M = map(int, input().split())

    a_list = []
    for i in range(N):
        a_list.append(list(map(int, input().split())))

    M, K = map(int, input().split())

    b_list = []
    for i in range(M):
        b_list.append(list(map(int, input().split())))

    multi_array = solution(N, M, a_list, K, b_list)

    for i in multi_array:
        for j in i:
            print(j, end=' ')
        print()
