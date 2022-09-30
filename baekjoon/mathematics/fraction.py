a = int(input())

line = 1

while a > line:
    a -= line
    line += 1

if (line % 2 == 0):
    up = a
    down = line - a + 1
else:
    up = line - a + 1
    down = a

print("{0}/{1}".format(up, down), sep="")

# 1. 1/1
# 2. 1/2, 2/1
# 3. 3/1, 2/2, 1/3
# 4. 1/4, 2/3, 3/2, 4/1
# 5. 5/1, 4/2, 3/3, 2/4, 1/5

