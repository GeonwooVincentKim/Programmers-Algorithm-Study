a = input().lower()
count_list = []

word_list = list(set(a))

for i in word_list:
    count = a.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(word_list[(count_list.index(max(count_list)))].upper())
