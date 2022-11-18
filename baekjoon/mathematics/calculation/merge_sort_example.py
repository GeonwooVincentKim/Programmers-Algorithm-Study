def merge_sort(array):
    def sort(low, high):
        if high - low < 2:
            return
        
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    
    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if array[l] < array[h]:
                temp.append(array[l])
                l += 1
            else:
                temp.append(array[h])
                h += 1

        while l < mid:
            temp.append(array[l])
            l += 1

        while h < high:
            temp.append(array[h])
            h += 1 

        for i in range(low, high):
            array[i] = temp[i - low]

    print(len(array))
    return sort(0, len(array))


if __name__ == "__main__":
    array = [4, 5, 1, 3, 2]
    # array = list(map(int, input().split()))
    print(merge_sort(array))
    # n, k = map(int, input().split())
