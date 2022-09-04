a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    get_avg = sum(b[1:]) / b[0]

    count = 0
    for c in b[1:]:
        if c > get_avg:
            count += 1
    
    rate = (count / b[0]) * 100
    print("%.3f" % rate + '%')
