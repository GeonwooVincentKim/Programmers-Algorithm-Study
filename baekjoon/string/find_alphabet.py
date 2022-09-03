a = input()
alphabet = []

for i in range(97, 123):
    alphabet.append(i)


for i in alphabet:
    print(a.find(chr(i)))


"""
1. input string
2. iterate from a to z
3. store the position of the alphabet
- 1. Save the location where the specific alphabet found
- 2. Store into the list

4. shows the location where it found for the first time.
"""
