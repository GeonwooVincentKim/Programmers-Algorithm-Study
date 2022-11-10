import math

# 소수 판별


def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

# 소수 찾기


def findPrimes(n):
    primes = []
    for i in range(2, n+1):  # for i in range(2, (n//2)+1) 로 개선 가능
        if isPrime(i):
            primes.append(i)
    return primes


print('소수 리스트', findPrimes(30))

# 소인수 분해 1


def factorize(n):
    factors = []
    primes = findPrimes(n)  # n의 소수 리스트를 추출
    for i in primes:
        while (n % i == 0):  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
            factors.append(i)
            n = n // i
    return factors


print('소인수분해 결과', factorize(3))
