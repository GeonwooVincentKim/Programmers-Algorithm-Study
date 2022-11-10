a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4 = b4 = 0

# If A1 and A2 value are same
if (a1 == a2):
    a4 = a3

# If A1 and A3 value are same
elif (a1 == a3):
    a4 = a2

# If A2 and A3 value are same
elif (a2 == a3):
    a4 = a1

if (b1 == b2):
    b4 = b3
elif (b1 == b3):
    b4 = b2
elif (b2 == b3):
    b4 = b1

print(a4, b4)



"""
1. x좌표 값을 저장할 a1, a2, a3 생성
2. y좌표 값을 저장할 b1, b2, b3 생성
3. x1, x2 좌표 값 개수 비교
- 1. 만약 1개이면 1개인 곳에 같은 값을 가지고 있는 숫자 추가
- 2. 만약 2개이면 통과

4. y1, y2 좌표 값 개수 비교
- 1. 만약 1개이면 1개인 곳에 같은 값을 가지고 있는 숫자 추가ㅣ
- 2. 만약 2개이면 통과
"""