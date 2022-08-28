a = b = 1
c = d = e = 2
f = 8

a1, b1, c1, d1, e1, f1 = map(int, input().split())
a2 = a - a1
b2 = b - b1
c2 = c - c1
d2 = d - d1
e2 = e - e1
f2 = f - f1
print("{0} {1} {2} {3} {4} {5}".format(a2, b2, c2, d2, e2, f2))
