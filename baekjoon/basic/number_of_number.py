a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c
get_value = str(multiply)

for i in range(10):
    print(get_value.count(str(i)))
