a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c
get_value = str(multiply)

k0 = k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = 0

for i in get_value:
    if (i.count('0')):  
        k0 += 1
    if (i.count('1')):
        k1 += 1
    if (i.count('2')):
        k2 += 1
    if (i.count('3')):
        k3 += 1
    if (i.count('4')):
        k4 += 1
    if (i.count('5')):
        k5 += 1
    if (i.count('6')):
        k6 += 1
    if (i.count('7')):
        k7 += 1
    if (i.count('8')):
        k8 += 1
    if (i.count('9')):
        k9 += 1

print(k0)
print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
print(k6)
print(k7)
print(k8)
print(k9)

# print(multiply)


# dp = [0] * 3
# dp[0] = a
# dp[1] = b
# dp[2] = c

# multiply = 0
# for i in range(len(dp)):
#     multiply *= dp[i]

# print(multiply)