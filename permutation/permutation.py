def solution(arr):
    print(len(arr))
    print(max(arr))
    return len(arr) == max(arr)

if __name__ == "__main__":
    print(solution([4, 1, 3]))
