def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    
    return abs(a)


if __name__ == "__main__":
    n = int(input())
    value_list = list(map(int, input().split()))

    for i in range(1, n):
        g = gcd(value_list[0], value_list[i])
        print('{0}/{1}'.format(value_list[0] // g, value_list[i] // g))
