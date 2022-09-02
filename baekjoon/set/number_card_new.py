import sys

a = int(input())
b = list(map(int, sys.stdin.readline().split()))

c = int(input())
d = list(map(int, sys.stdin.readline().split()))

b.sort()


def binary_search(target, start, end, data):
    while start <= end:
        mid = (start + end) // 2

        if (data[mid] == target):
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None


if __name__ == "__main__":
    for i in range(c):
        if binary_search(d[i], 0, a - 1, b) is not None:
            print(1, end=' ')
        else:
            print(0, end=' ')

"""
1. a, b, c, d 입력
2. 상근의 list 정렬
3. 상근의 list 를 가지고 온 후, 내 list 와 겹치는 것들이 있는지 확인
- 2. 겹치는 숫자는 1
- 3. 겹치지 않는 숫자는 0

4. Target List, Data List 각각 main part 에서 대입
5. 겹치는 숫자와 겹치지 않는 숫자 비교
"""
