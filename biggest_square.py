def solution(board):
    print(board)
    print(board[0])

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j-1], board[i-1][j]) + 1

    answer = 0
    for i in range(len(board)):
        temp = max(board[i])
        answer = max(answer, temp)

    return answer ** 2
    # x = []

    # for x in board:
    #     print(x)
    # print(board[0])


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
