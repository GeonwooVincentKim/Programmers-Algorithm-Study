a = int(input())

for i in range(a):
    number, string = input().split()
    
    for j in string:
        print(j*int(number), end="")
    print()
