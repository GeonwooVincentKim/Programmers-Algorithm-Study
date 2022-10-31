a = int(input())

before_sort_list = list(map(int, input().split()))
s = int(input())


def bubble_sort(arr, stop):
    end = len(arr) - 1

    for i in range(end):

        if stop == 0:
            break
        
        get_max, last_swap = arr[i], i
        for j in range(i + 1, min(len(arr), i + 1 + stop)):
            if get_max < arr[j]:
                get_max = arr[j]
                last_swap = j
        
        stop -= last_swap - i
        for j in range(last_swap, i, -1):
            arr[j] = arr[j - 1]
        
        arr[i] = get_max
    
    print(*arr)

        
bubble_sort(before_sort_list, s)
