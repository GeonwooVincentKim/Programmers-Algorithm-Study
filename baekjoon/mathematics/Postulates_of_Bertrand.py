import sys
import math


def isPrime(num):
    if num == 1:
        return 0
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return 0
    return 1


while 1:
    a = int(sys.stdin.readline())
    
    if a == 0:
        break

    cnt = 0
    for i in range(a + 1, 2 * a + 1):
        if isPrime(i):
            cnt += 1
    
    print(cnt)
