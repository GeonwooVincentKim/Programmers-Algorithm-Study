def hanoi(n, src, distance):
    temp = 6 - src - distance
    
    if n == 0:
        return
    
    hanoi(n - 1, src, temp)
    print(src, distance)
    hanoi(n - 1, temp, distance)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)
