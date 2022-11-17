t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    interval = 1
    count = 0

    interval_sum = 0

    while interval_sum < distance:
        count += 1
        interval_sum += interval

        if count % 2 == 0:
            interval += 1

    print(count)
