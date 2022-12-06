import sys

fibo = [0 for _ in range(101)]
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1

a = 0
n = int(sys.stdin.readline())
b = n

while True:
    for i in range(3, 100):
        fibo[i] = fibo[i-1] + fibo[i-2]
        
        if fibo[i] > n:
            n -= fibo[i-1]
            break
        if fibo[i] == b:
            print(-1)
            a = 1
            break
        if fibo[i] == n:
            a = 1
            print(n)
            break

    if a == 1:
        break
