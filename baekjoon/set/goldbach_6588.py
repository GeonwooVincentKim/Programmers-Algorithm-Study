array = [True for _ in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(input())

    if n == 0:
        break

        # if array[i] == True:
        #     j = 2

        #     while i * j <= n:
        #         array[i * j] = False
        #         j += 1

    for i in range(3, len(array)):
        if array[i] == True:
            if array[n - i] == True:
                print("%d = %d + %d" % (n, i, n - i))
                break
"""
1. Get the user input-value
2. Iterate from 1 to user input-value
- 1. Example) If user input 8, iterate 1 to 8
- 2. Get the minority value
- 3. Plus between two minority value
  = 1. Check plus two minority value equals to user input value (For example 8), 
  = 2. Store into the answer area's list
"""
