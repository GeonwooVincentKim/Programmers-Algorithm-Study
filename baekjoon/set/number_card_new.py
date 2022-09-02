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
3. 상근의 list 와 내 list 서로 비교
4. 
"""
