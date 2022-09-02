def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if (data[mid] == target):
            return mid
        # If data[mid] is smaller than target number
        elif data[mid] < target:  
            start = mid + 1  # Increase the starting position by 1
        else:
            end = mid - 1
    
    return None


if __name__ == "__main__":
    li = [i ** 2 for i in range(11)]
    target = 9
    idx = binary_search(target, li)

    if idx:
        print(li[idx])
    else:
        print('The element {0} that you looking for does not exist'.format(target))
