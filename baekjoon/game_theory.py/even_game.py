n, k = map(int, input().split())

"""
    The way No.1
"""
print("HS" if n == 0 and k % 6 == 1 else "HS" if n == 1 and k % 6 != 1 and k % 6 != 2 and k % 6 != 3 and k % 6 != 4 else "YG")

"""
    The way No.2
"""
# if n == 0:
#     print("HS" if k % 6 == 1 else "YG")
# else:
#     print("HS" if k % 6 == 0 or k % 6 == 5 else "YG")
