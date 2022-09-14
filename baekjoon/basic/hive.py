a = int(input())

num_set = 1
count = 1

while a > num_set:
    num_set += 6 * count
    count += 1

print(count)
