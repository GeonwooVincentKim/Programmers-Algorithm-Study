a = int(input())
result = 1

for item in range(1, a + 1, 1):
    result *= item

get_string = list(str(result))

count = 0
for i in get_string:
    print(i)

print(get_string.count('0'))
