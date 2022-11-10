import math

while True:
    result = True
    n = int(input())
    array = [True for _ in range(n + 1)]

    if n == 0:
        break

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2

            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if array[i]:
            print(i, end=' ')
    print()

"""
1. Get the user input-value
2. Iterate from 1 to user input-value
- 1. Example) If user input 8, iterate 1 to 8
- 2. Get the minority value
- 3. Plus between two minority value
  = 1. Check plus two minority value equals to user input value (For example 8), 
  = 2. Store into the answer area's list
"""
