n = int(input())

list = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            list[i][j] = 1

count = 0
for row in list:
    count += row.count(1)

print(count)

"""
1. Input the number of Color Paper
2. Input coord x and coord y
3. 
(1) x = (3 + 10), y = (7 + 10) -> x = 3 ~ 13, y = 7 ~ 17
(2) x = (15 + 10), y = (7 + 10) -> x = 15 ~ 25, y = 7 ~ 17
(3) x = (5 + 10), y = (2 + 10) -> x = 5 ~ 15, y = 2 ~ 12

4. Store each x, y values into list
5. Check collision between two rectangles
- 1. Get (1) value and (3) value
- 2. x[0] -> x = 3, x[0][0] -> x = 3, x[1][0] -> x = 13
- 3. if((x[0][0] > x[2][0]) && (x[0][1] < x[2][1]) && (y[0][0] > y[2][0]) && (y[0][1] < y[2][1]))
- 4. Minus the differences
  = 1. (x[2][0] - x[0][0])
    -> 5 - 3 = 2

  = 2. (x[2][1] - x[0][1])
    -> 
  = 3. (y[2][0] - y[0][0])
  = 4. (y[2][1] - y[0][1])
"""
