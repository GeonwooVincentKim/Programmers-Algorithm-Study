def solution(sizes):
    w = []
    h = []

    for a, b in sizes:
        if (a < b):
            swap = b
            b = a
            a = swap            

        w.append(a)
        h.append(b)

    getSum = max(w) * max(h)
    return getSum


if __name__ == "__main__":
    solution([[60, 50], [30, 70], [60, 30], [80, 40]])
    solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
    solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])

# 1. 각 List 안에 있는 중첩 List 의 값들을 뽑아온다.
# 2. 뽑아온 중첩 List 의 값들을 서로 비교 후, 큰 수는 앞으로, 작은 수는 뒤로 보낸다
# 3. 중첩 List 의 값들을 각각 w 와  h 로 분리한다.
# 4. 중첩 List 에서 각각 w 와  h 로 분리한 값들 중 max(w), max(h) 와 같은 형태로 구성한다.

60, 50
70, 30 # switch position
60, 30
80, 40


10, 7
12, 3
15, 8 # switch position
14, 7
15, 5 # switch position


14, 4
19, 6
16, 6 # switch position
18, 7
11, 7 # switch position
