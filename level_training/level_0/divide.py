def solution(num1, num2):
    result = int(num1 / num2 * 1000)
    return result

if __name__ == "__main__":
    print(solution(3, 2))
    print(solution(7, 3))
    print(solution(1, 16))
