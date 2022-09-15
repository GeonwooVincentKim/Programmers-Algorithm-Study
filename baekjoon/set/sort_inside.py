a = input()
a_list = []

for i in range(len(a)):
    a_list.append(a[i])
a_list.sort(reverse=True)

for i in a_list:
    print(i, end="")
