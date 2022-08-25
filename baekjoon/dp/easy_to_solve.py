# a, b = map(int, input().split())

# sum = 0
# for i in range(a + 1, b):
#     sum += i

# print(sum)

a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))
