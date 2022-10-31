N, M = map(int, input().split())

a_list = []
for i in range(N):
    a_list.append(list(map(int, input().split())))

M, K = map(int, input().split())

b_list = []
for i in range(M):
    b_list.append(list(map(int, input().split())))


answer_list = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            answer_list[i][j] += a_list[i][k] * b_list[k][j]

for i in answer_list:
    for j in i:
        print(j, end=' ')
    print()
