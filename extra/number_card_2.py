def binary_search_list(target, data, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if (data[mid] == target):
        return data[start:end + 1].count(target)
    elif data[mid] > target:
        return binary_search_list(target, data, start, mid - 1)
    else:
        return binary_search_list(target, data, mid + 1, end)


if __name__ == "__main__":
    a = int(input())
    b = list(map(int, input().split()))

    c = int(input())
    d = list(map(int, input().split()))
    b.sort()

    _dict = {}

    for j in b:
        start = 0
        end = len(b) - 1
        if j not in _dict:
            _dict[j] = binary_search_list(j, b, start, end)
    
    print(' '.join(str(_dict[x]) if x in _dict else '0' for x in d))
