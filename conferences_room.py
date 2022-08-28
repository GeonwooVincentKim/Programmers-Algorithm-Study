from collections import Counter

def solution(info):
    print(info)

    a = b = 0
    i2 = j2 = 0
    storeCount = []

    # dp = [[0]*2 for _ in range(len(info))]
    # dp = [[0 for j in range(info[i])] for i in range(info)]
    # print(dp)

    # for i in info:
    #     dp = [[0 for j in range(info[i])] for i in range(info)]
    #     print(dp)
    for i, j  in info:
        i2 = i
        j2 = j
    
    dp = [[0 for j3 in range(i)] for i3 in range(j)]
    print(dp)
    
    a = dp[i][0]
    b = dp[i][1]

    print(a, b)

    # for i in range(len(info)):
    #     for j in range(len(info[i])):
    #         a = info[i][0]
    #         b = info[i][1]
    #         # a = dp[i][0]
    #         # b = dp[i][1]

    #     print(a, b)

    #     for k in range(a, b + 1):
    #         # print(k)
    #         storeCount.append(k)

                
    #         # print(storeCount)
    #         # cnt = storeCount.count(k)
    #         # getCount.append(storeCount.count(k))

    # checkCount = []
    # duplicateCount = []

    # for k1 in storeCount:
    #     if k1 not in checkCount:
    #         checkCount.append(k1)
    #     else:
    #         if k1 not in duplicateCount:
    #             duplicateCount.append(k1)

    #     # return duplicateCount
    
    # print(duplicateCount)

    # answer = []
    # return answer


if __name__ == "__main__":
    solution([[1, 5], [3, 5], [7, 8]])
    solution([[2, 3], [2, 5], [2, 2], [3, 3]])
    solution([[1, 2], [2, 3], [4, 5], [5, 6]])

# 1. info 전체 List 를 불러온다
# 2. info 내 중첩 list 의 값들을 차례대로 출력한다
# -> ex) [1, 5] => [1, 2, 3, 4, 5]

# 3. info 내 중첩 list 의 값들을 count 시키는 변수 하나 생성
# -> ex) [1, 5] -> 1 ~ 5 값 각각 카운트 1회씩 실시 -> 1 ~ 5 까지의 count = 1
# -> ex) [3, 5] -> 3 ~ 5 값 각각 카운트 1회씩 실시 -> 3 ~ 5 까지의 count = 2
# -> ex) [7, 8] -> 7 ~ 8 값 각각 카운트 1회씩 실시 -> 7 ~ 8 까지의 count = 1

# 4. 숫자별 각 count 숫자 비교 후, 가장 많이 나왔던 count 를 answer list 에 append
