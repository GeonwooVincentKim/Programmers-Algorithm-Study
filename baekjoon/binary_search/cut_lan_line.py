k, n = map(int, input().split())

lan_list = []
for i in range(k):
    inner = int(input())
    lan_list.append(inner)

start, end = 1, max(lan_list)

while start <= end:
    mid = (start + end) // 2

    log = 0
    for i in lan_list:
        log += i // mid

    if log >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
