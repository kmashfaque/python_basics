arr = [2, 1, 4, 5, 7, 8, 6, 9, 2, 3, 10]


def bubble_sort(data):
    for i in range(0, len(arr)):
        for j in range(0, (len(arr)-1)):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


bubble_sort(arr)
