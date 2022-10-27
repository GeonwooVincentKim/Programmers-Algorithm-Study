# # def solution(array, commands):
# #     i = j = 0

# #     for outer in range(len(commands)):
# #         for inner in range(len(commands[outer])):
# #             i = commands[outer][0]
# #             j = commands[outer][1]

# #         getArray = array[i - 1:j]
        
# #         if (isPalindrome(getArray) == True):
# #             print(1)
# #         else:
# #             print(0)


# import sys
# input = sys.stdin.readline


# # def isPalindrome(value):
# #     return value == value[::-1]


# length = int(input())
# number_list = list(map(int, input().split()))

# m = int(input())
# dp = [[0] * length for _ in range(length)]

# # def solution(dp, length, num_list):
# #     for outer in range(length):
# #         for inner in range(length - outer):
# #             end = inner + outer

# #             if(inner == end):
# #                 dp[inner][end] = 1
# #             elif(num_list[inner] == num_list[end]):
# #                 if inner + 1 == end:    dp[inner][end] = 1
# #                 elif dp[inner+1][end+1] == 1:   dp[inner][end] = 1

# #     print(dp[s-1][e-1])

# for outer in range(length):
#     for inner in range(length - outer):
#         end = inner + outer

#         if inner == end:
#             dp[inner][end] = 1
#         elif number_list[inner] == number_list[end]:
#             if inner + 1 == end:    
#                 dp[inner][end] = 1
#             elif dp[inner+1][end+1] == 1:   
#                 dp[inner][end] = 1

# for q in range(m):
#     s, e = map(int, input()).split()
#     print(dp[s-1][e-1])
# # member_list = [list(map(int, input().split())) for _ in range(m)]
# # print(member_list)
# # solution(number_list, member_list)

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

#dp
dp = [[0] * n for _ in range(n)]


for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len
        
        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
        	# 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end: dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1: dp[start][end] = 1
            

#정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
