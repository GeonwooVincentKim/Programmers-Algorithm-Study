croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=', ]

alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

print(alphabet)

count = 0

a = input()
for i in croatian_alphabet:
    a = a.replace(i, '*')
    print(a)

print(len(a))
# if croatian_alphabet in a:
#     count += 1
# for j in range(len(a)):
#     for i in croatian_alphabet:




"""
1. Input string
2. Generate Croatian Alphabet
3. Generate Normal Alphabet
4. Replace the croatian alphabet to `*`
"""

# a = 'hello world'
# b = a.replace('hello', 'hi')
# print(b)
