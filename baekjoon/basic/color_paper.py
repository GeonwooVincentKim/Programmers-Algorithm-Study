import sys
a = int(sys.stdin.readline())

color_paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
blue = []
white = []

def Color(x, y, n):
    check = color_paper_list[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != color_paper_list[i][j]:
                Color(x, y, n // 2)
                Color(x + n // 2, y, n // 2)
                Color(x, y + n // 2, n // 2)
                Color(x + n // 2, y + n // 2, n // 2)
                return
    
    if check == 1:  
        blue.append(n ** 2)
    else:  
        white.append(n ** 2)

    return

Color(0, 0, a)
print(len(white))
print(len(blue))
