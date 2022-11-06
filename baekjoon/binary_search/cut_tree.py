a, b = map(int, input().split())
get_list = list(map(int, input().split()))

start, end = 1, max(get_list)

while start <= end:
    mid = (start + end) // 2

    log = 0
    for i in get_list:
        if i >= mid:
            log += i - mid

    if log >= b:
        start = mid + 1
    else:
        end = mid - 1

print(end)
