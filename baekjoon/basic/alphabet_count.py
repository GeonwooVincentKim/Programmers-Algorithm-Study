a = input()

for i in range(0, 26):
    res = a.count(chr(i + ord('a')))
    print(res, end=' ')
