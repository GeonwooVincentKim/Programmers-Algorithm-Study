from itertools import combinations
# arr = ['a', 'b', 'c', 'd']
# arr = [2, 2]
# arr = [13, 29]
# print(combinations(arr, 2))

arr = []
# a, b = map(int, input().split())

for i in range(1, 5):
    arr.append(i)


for i in combinations(arr, 2):
    print(i, end=" ")

print(len(list(combinations(arr, 2))))

# arr2 = []
# for i in range(13, 29):
#     arr.append(i)

# print(len(list(combinations(arr, 2))))

# arr = []
# for i in range(13, 30):
#     arr.append(i)

# def combination(arr, r):
#     # 1.
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     # 2.
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#     	# 3.
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
#                 chosen.append(arr[nxt])
#                 used[nxt] = 1
#                 generate(chosen)
#                 chosen.pop()
#                 used[nxt] = 0
#     generate([])

# print(combination(arr, len(arr)))

# def permutation(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in permutation(arr[:i] + arr[i+1:], n - 1):
#             result.append([elem] + rest)
#     return result
    
# print(permutation([0,1,2,3], 2))
# print(len(permutation(arr2, 2)))
