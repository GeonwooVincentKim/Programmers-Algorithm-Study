def solution(array, commands):
    i = j = 0

    for outer in range(len(commands)):
        for inner in range(len(commands[outer])):
            i = commands[outer][0]
            j = commands[outer][1]

        getArray = array[i - 1:j]
        
        if (isPalindrome(getArray) == True):
            print(1)
        else:
            print(0)


def isPalindrome(value):
    return value == value[::-1]


length = int(input())
number_list = list(map(int, input().split()))

m = int(input())
member_list = [list(map(int, input().split())) for _ in range(m)]

solution(number_list, member_list)

