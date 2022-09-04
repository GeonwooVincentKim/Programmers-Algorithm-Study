a = int(input())

for i in range(a):
    b = input()
    sum = 0
    con_sum = 0

    for j in range(len(b)):
        if b[j] == "O":
            sum += 1
            con_sum += sum
        
        elif b[j] == "X":
            sum = 0
        
    print(con_sum)
    

"""
1. Input b as a
2. Split the string
3. If there is O, count sum as 1
4. If the O are consecutive, count `con_sum += sum`
"""