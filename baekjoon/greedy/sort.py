a = int(input())

before_sort_list = list(map(int, input().split()))
s = int(input())


def bubble_sort(arr, stop):
    end = len(arr) - 1

    while end > 0:
        last_swap = 0

        for i in range(end):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
            
            if i == (stop - 1):
                break

        end = last_swap

    return arr
        
        
get_value = bubble_sort(before_sort_list, s)
print(get_value)
