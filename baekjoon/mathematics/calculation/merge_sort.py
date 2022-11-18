import sys


def merge_sort(array, left, right):
    if (left < right and count <= k):
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
        

def merge(array, left, mid, right):
    global result, count

    i, j = left, mid + 1
    temp = []

    while (i <= mid and j <= right):
        if (array[i] <= array[j]):
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1
    
    while j <= right:
        temp.append(array[j])
        j += 1    

    i, t = left, 0

    while i <= right:
        array[i] = temp[t]
        count += 1

        if count == k:
            result = array[i]
            break
            
        i += 1
        t += 1
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    array_list = list(map(int, sys.stdin.readline().split()))

    count = 0
    result = -1
    merge_sort(array_list, 0, n - 1)
    print(result)
