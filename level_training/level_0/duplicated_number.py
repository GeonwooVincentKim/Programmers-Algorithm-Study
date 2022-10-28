def solution(array, n):
    count = array.count(n)
    return count

if __name__ == "__main__":
    print(solution([1, 1, 2, 3, 4, 5], 1))
    print(solution([0, 2, 3, 4], 1))
