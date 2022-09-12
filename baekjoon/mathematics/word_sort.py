a = int(input())
word_sort = [input() for _ in range(a)]

word_sort = list(set(word_sort))
word_sort.sort()
word_sort.sort(key=lambda x: len(x))

for i in word_sort:
    print(i)
# print(word_sort.sort(key=len))

