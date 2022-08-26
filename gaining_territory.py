def solution(land):
    # One `dp` can lots of data input into this list.
    # dp = [0] * 100000

    d = [[i for i in land[0]]] # Get first inner-list elements
    d.extend([[0] * 4 for _ in range(len(land) - 1)]) # Generate new inner-list that follows the size of list that user declared from main

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            a, b, c = [jj for jj in range(4) if jj != j]  # The selected number cannot step on the same column consecutively.
            d[i][j] = land[i][j] + max(d[i-1][a], d[i-1][b], d[i-1][c])
            # print(d[i][j])
            print(max(d[i-1][a], d[i-1][b], d[i-1][c]))
    
    return max(d[-1])


    # dp = [[0] * 4 for i in range(land)]
    # print(dp)
    # for i in range(1, len(land)):
    #     for j in range(4):
            

    # answer = 0
    # return answer


if __name__ == "__main__":
    solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
