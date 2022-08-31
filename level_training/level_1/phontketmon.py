def solution(nums):
    answer = 0
    length = len(nums) // 2
    temp = list(set(nums))

    for value in temp:
        if (answer < length):
            answer += 1
    
    return answer


if __name__ == "__main__":
    solution([3, 1, 2, 3])
    solution([3, 3, 3, 2, 2, 4])
    solution([3, 3, 3, 2, 2, 2])
