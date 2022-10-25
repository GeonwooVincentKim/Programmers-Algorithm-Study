croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=', ]

a = input()
for i in croatian_alphabet:
    a = a.replace(i, '*')

print(len(a))

"""
1. Input string
2. Generate Croatian Alphabet
3. Generate Normal Alphabet
4. Replace the croatian alphabet to `*`
"""

# a = 'hello world'
# b = a.replace('hello', 'hi')
# print(b)
