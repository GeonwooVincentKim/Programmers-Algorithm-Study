def binary_search_list(target, data, start=0, end=None):
    if end == None:
        end = len(data) - 1
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if (data[mid] == target):
        return 1
    elif (data[mid] < target):
        start = mid + 1
    else:
        end = mid - 1

    return binary_search_list(target, data, start, end)

if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()

    n2 = int(input())
    m2 = list(map(int, input().split()))

    for i in range(len(m2)):
        print(binary_search_list(m2[i], m))
