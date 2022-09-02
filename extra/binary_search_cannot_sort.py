def binary_search_list(target, data):
    start = 0
    data.sort()
    end = len(data) - 1
    print(target, data)

    while start <= end:
        mid = (start + end) // 2
        
        if (data[mid] == target):
            return mid
        elif (data[mid] < target):
            start = mid + 1
        else:
            end = mid - 1

    return None


get_list = [12, 25, 21, 18, 35, 18, 8]
target = 21
get_value = binary_search_list(target, get_list)

if (get_value):  print(get_list[get_value])
else:   print("찾으려는 {0} 가 존재하지 않습니다.".format(target))
