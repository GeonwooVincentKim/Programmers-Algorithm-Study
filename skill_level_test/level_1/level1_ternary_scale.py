def solution(n):
    answer = 0
    get_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        get_base += str(mod)

    n = get_base[::-1]
    n = n[::-1]

    answer = int(n, 3)

    return answer


if __name__ == "__main__":
    print(solution(21))
