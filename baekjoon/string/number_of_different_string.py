s = input()
get_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j + 1]
        get_set.add(temp)

print(len(get_set))
