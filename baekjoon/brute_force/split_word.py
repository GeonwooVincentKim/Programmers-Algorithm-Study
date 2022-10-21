import sys

a = list(input())
store_list = []

for i in range(1, len(a) - 1):
    for j in range(i + 1, len(a)):
        inner_a = a[:i]
        inner_b = a[i:j]
        inner_c = a[j:]

        inner_a.reverse()
        inner_b.reverse()
        inner_c.reverse()
        store_list.append("".join(inner_a + inner_b + inner_c))

print(min(store_list))
