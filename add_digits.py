def solution(n):
    sum = 0
    while(int(n) != 0):
        sum += (int(n) % 10)
        n = int(n) / 10
    
    return int(sum)
