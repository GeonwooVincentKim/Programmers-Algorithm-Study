arr = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]
print(arr)

m = 4
n = 3

sum_arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_arr[i][j] = arr[i - 1][j - 1] + (sum_arr[i - 1][j]) + (sum_arr[i][j - 1]) - (sum_arr[i - 1][j - 1])

print('sum_arr : ')
for i in range(n + 1):
    print(sum_arr[i])
