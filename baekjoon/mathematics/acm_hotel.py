a = int(input())

for i in range(a):
    h, w, n = map(int, input().split())
    num = (n // h) + 1
    floor = n % h

    if (floor == 0):
        floor = h
        num -= 1
    
    print(floor * 100 + num)


## 0. h = 각각 호텔의 층 수, w = 각 층의 방 수, n = 몇 번째 손님
## 1. h, w, n 입력
## 2. 손님이 머물 층 수와 방의 위치를 구합니다.
## 여기서는 w 라는 변수를 입력받지만, 사용하지 않고 있습니다.
## num = (n // h) + 1
## floor = n % h

## 3. 층수가 만약 0이라면 floor 는 h 로부터 값을 받아오고, num 을 1을 감소하여 현재 층수를 구한다.
## 4. 방의 숫자가 100 단위로 진행하므로, floor 에 100 을 곱한 후, 손님 순서를 뒤에 더하여 방 수를 출력한다.

