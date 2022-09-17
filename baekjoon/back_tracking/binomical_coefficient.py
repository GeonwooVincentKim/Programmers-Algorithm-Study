def factorial(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    return answer


def binomical_coefficient_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


a, b = map(int, input().split())
print(binomical_coefficient_factorial(a, b))
