arr = [2, 1, 4, 5, 7, 8, 6, 9, 2, 3, 10]


def insertion_sort(data):
    for i in range(1, len(arr)):
        j = i
        curr_elm = arr[j]
        while j > 0 and curr_elm < arr[j-1]:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = curr_elm

    print(arr)


def insertion_sort_1(data):
    for i in range(1, len(arr)):
        curr_elm = arr[i]
        while i > 0 and curr_elm < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1
    print(arr)


insertion_sort(arr)
insertion_sort_1(arr)
