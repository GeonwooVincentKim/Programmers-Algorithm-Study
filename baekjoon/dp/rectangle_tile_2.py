def solution(n):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    return dp[n]
    

if __name__ == "__main__":
    n = int(input())
    print(solution(n) % 10007)
