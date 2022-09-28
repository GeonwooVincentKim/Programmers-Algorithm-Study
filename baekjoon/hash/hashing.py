a = int(input())
b = input()

r = 31
m = 1234567891
number = 0

for i in range(len(b)):
    value = ord(b[i]) - 96
    number += value * (r ** i)

print(number % m)

