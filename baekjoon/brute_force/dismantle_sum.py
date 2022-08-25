a = int(input())
total = 0

for i in range(a):
    inner_num = i
    sum = 0

    while (int(inner_num) > 0):
        sum += int(inner_num) % 10
        inner_num /= 10
    
    if (sum + i == a):
        total = i
        break

print(total)
