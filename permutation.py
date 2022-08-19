def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    arr.sort()
    
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return False
            
    return True
