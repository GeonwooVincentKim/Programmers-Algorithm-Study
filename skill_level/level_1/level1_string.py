def solution(s):
    countY = 0
    countP = 0

    for i in range(len(s)):
        if (s[i].count('y') == s[i].count('p')):
            return True
        elif (s[i].count('y') != s[i].count('p')):
            return False
        else:
            return True


if __name__ == "__main__":
    print(solution("pPoooyY"))
    print(solution("Pyy"))
