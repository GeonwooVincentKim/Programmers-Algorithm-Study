def factorial(n):
    answer = 1
    
    for i in range(2, n + 1):
        answer *= i
    return answer


def binomical_coeffcient_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n - r) % 10007


a, b = map(int, input().split())
print(binomical_coeffcient_factorial(a, b))
