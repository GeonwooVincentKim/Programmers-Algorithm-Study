a = int(input())

b_list = []

for i in range(a):
    b_list.append(list(map(int, input().split())))

## If it arrange while iterate in the `for loop`
## compiler takes lot of time to calculate sorted value
b_list.sort() 

for j in b_list:
    print("{0} {1}".format(j[0], j[1]))

# 1. Input the Matrix as the number of a
# 2. Store each Matrix into new List
# 3. Split Matrix x and y
# 4. Compare value x from each Matrix
# 5. If value x has a same value, compare value y
