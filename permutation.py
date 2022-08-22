# 1. 중복 없음 -> 정렬 우선 진행
# 2. 한 번씩만 있을 경우 = True
# 3. 여러 개 있거나 없을 경우 = False

def solution(arr):
    # answer = True

    for i in range(len(arr)):
        if (i + 1 != arr[i]):
            # print("True")
            # print("False")
            return False
            # return False

    # print("True")
    return True
    # print(arr[i])

    # return answer


if __name__ == "__main__":
    print(solution([4, 1, 3, 2]))
