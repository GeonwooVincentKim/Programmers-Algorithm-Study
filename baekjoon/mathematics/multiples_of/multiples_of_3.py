a = int(input())
value_list = list(map(int, str(a)))
# print(value_list)

count = 0
while True:
    if len(value_list) == 1:
        inner_sum = value_list[0]
        break

    count += 1

    inner_sum = 0
    for i in value_list:
        inner_sum += i

    if inner_sum < 10:
        break
    else:
        value_list = list(map(int, str(inner_sum)))

if count == 3 or count == 6 or count == 9:
    print(i)
    print("YES")
else:
    print(i)
    print("NO")

# count = 0
# while True:
#     if a % 3 == 0:
