def solution(arr):
    answer = []
    
    for i in arr:
        if answer[-1:] == [i]:   continue
        answer.append(i)
    
    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))
    print(solution([4, 4, 4, 3, 3]))
