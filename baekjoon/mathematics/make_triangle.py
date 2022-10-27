a = int(input())
count = 0

for x in range(1, a):
    for y in range(x, a):
        z = a - x - y

        if (y > z): break
        if (x + y > z): count += 1

print(count)

"""
1. An isoceles triangle
- 1. The two sides of triangle are equal in length
- 2. The two sides triangle sum should be bigger than other side of triangle length

2. A right-angled triangle
- Pythagorean theorem

3. Regular triangle
- Every side of triangle shoudl equal in length

**
1. Get the other side of triangle length
2. 
"""