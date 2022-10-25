a = int(input())

count = 0
while a >= 0:
    if a % 5 == 0:
        count += (a // 5)
        print(count)
        break

    a -= 3
    count += 1

    if a < 0:
        print(-1)
        break

"""
Bring a minimal plastic bag
1. Use Greedy Algorithm to solve this issue
2. Declare list variable name `list` which includes the sort of weight of plastic bag
- 1. 3kg
- 2. 5kg
- 3. --> [3, 5]

3. count the number of plastic bag
- 1. count += a // bag
- 2. a %= bag

1. Input `a`
2. Stop iterate if `a` less smaller than 0
3. Count with multiple of 5 
- 1. if the separated value become Integer Number (Not Minority), count += (a // 5)
- 2. print bag and break the loop

4. Minus 3 from `a` value
- If you count with multiple of 3, The number such as 18, or 21 only count the multiple of 3, 
  So do not use this way If you want to get a minimum count.

5. Count 1 if `a` value stil remained
6. if `a` value smaller than 0, print `-1` and break the loop
"""