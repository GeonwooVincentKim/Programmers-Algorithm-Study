def solution(n):
    sum = 0
    a = int(n)

    while(a != 0):
        sum += (a % 10)
        n = a / 10
    
    return int(sum)


if __name__ == "__main__":
    print(solution(328))
