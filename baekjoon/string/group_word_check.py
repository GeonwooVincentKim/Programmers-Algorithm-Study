import sys
input = sys.stdin.readline

a = int(input())
count = 0

for i in range(a):
    word = input()
    check = True

    for j in range(len(word) - 1):
        if (word[j] != word[j + 1]):
            if (word[j] in word[j + 1:]):
                check = False
                break

    if (check == True):
        count += 1

print(count)

"""
abcd -> true
string[i] != string[i + 1]

abccd -> true
- 1. string[i] != string[i + 1]
- 2. string[i] is string[i + 1:] 
  = 1. Compare current value and next value, and iterate it 
  = 2. If it found the current value and iterate value (current value index: 0, next value index: 2)
       leave For-Loop area

abab -> false



"""