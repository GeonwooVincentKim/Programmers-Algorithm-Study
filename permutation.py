def solution(arr):
    arr.sort()
    
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return False
            
    return True


if __name__ == "__main__":
    print(solution([4, 1, 3, 2]))
