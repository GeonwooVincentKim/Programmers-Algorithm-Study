from itertools import permutations


def solution(numbers):
    answer = 0
    case = makeCase(numbers)
    for n in case:
        if isPrime(n):
            answer += 1

    return answer


def makeCase(numbers):
    result = []
    for i in range(1, len(numbers)+1):
        result.extend(list(map(int, map(''.join, permutations(numbers, i)))))
    result = list(filter(lambda x: x > 1, list(set(result))))

    return result


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(solution("17"))
    print(solution("011"))
