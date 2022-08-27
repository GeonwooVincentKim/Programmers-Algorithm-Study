def solution(array, commands):
    i = j = k = 0
    result = []

    for outer in range(len(commands)):
        for inner in range(len(commands[outer])):
            i = commands[outer][0]
            j = commands[outer][1]
            k = commands[outer][2]
        
        sortArray = array[i - 1:j]
        sortArray.sort()
        getIndex = sortArray[k - 1]
        result.append(getIndex)

        # sortedArray = sorted(array[i - 1:j])   
        # getIndex = sortedArray[k - 1]
        # result.append(getIndex)
    
    # print(sortArray)
    print(result)
    # return result


if __name__ == "__main__":
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7 ,3]])


# 1. array 정렬
# 2. commands 에 나온 list 를 각각 분리, 0번째 index 부터 2번째 index 까지 차례대로 분리
# 3. commands 에서 분리한 list 의 원소를 하나하나씩 가지고 옴

# 4. commands 의 첫 번째 list 의 원소 값을 각각 i, j, k 의 값으로 넣기 (commands 의 중첩 List 의 총 개수 길이만큼 순회)
# ex) i = 2, j = 5, k = 3

# 5. python slice 활용, array list 의 값을 가지고 오기
# 6. [::] 에 각각 [i:j:k] 의 값을 넣기
# 7. 순회 중인 곳에서 print(array[i:j:k]) 와 같은 형태로 출력하기

