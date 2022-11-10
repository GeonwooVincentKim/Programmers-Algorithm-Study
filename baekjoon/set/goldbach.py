"""
Number 1    
"""


def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1


"""
Number 2
"""

array = [True for _ in range(10001)]

for i in range(2, 10001):
    if array[i]:
        for k in range(i + i, 10001, i):
            array[k] = False


t = int(input())

count = 0
while t:
    num = int(input())

    # Iterate to opposite way (num -> 0)
    for i in range(num // 2, 0, -1):
        if array[i] == True:
            if array[num - i] == True:
                print(i, num - i)
                break

    # If Count number and Test Case number are same
    # Escape from the While Loop
    if count == (t - 1):
        break
    else:
        count += 1
