def isPalindrome(value):
    return value == value[::-1]  # Check Palindrome or not


while True:
    a = input()

    if (a == '0'):
        break

    if (isPalindrome(a) == True):
        print("yes")
    else:
        print("no")

