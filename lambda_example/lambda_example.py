def general_way(index):
    return index * 3


def solution(numbers):
    get_list = list(map(str, numbers))
    get_list.sort(key=general_way, reverse=True)
    return str(int(''.join(get_list)))


if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
