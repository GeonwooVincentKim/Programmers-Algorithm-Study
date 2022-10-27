# def solution(array, commands):
#     i = j = 0

#     for outer in range(len(commands)):
#         for inner in range(len(commands[outer])):
#             i = commands[outer][0]
#             j = commands[outer][1]

#         getArray = array[i - 1:j]
        
#         if (isPalindrome(getArray) == True):
#             print(1)
#         else:
#             print(0)


import sys
input = sys.stdin.readline

length = int(input())
number_list = list(map(int, input().split()))

m = int(input())
dp = [[0] * length for _ in range(length)]


def solution(length, number_list, dp):
    for outer in range(length):
        for inner in range(length - outer):
            end = inner + outer

            if inner == end:
                dp[inner][end] = 1
            elif number_list[inner] == number_list[end]:
                if inner + 1 == end:    
                    dp[inner][end] = 1
                elif dp[inner + 1][end - 1] == 1:   
                    dp[inner][end] = 1


solution(length, number_list, dp)

for q in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
