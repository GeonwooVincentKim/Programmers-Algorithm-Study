a, b = input().split()
a_list = a[::-1]
b_list = b[::-1]

if a_list > b_list:
    print(a_list)
elif a_list < b_list:
    print(b_list)