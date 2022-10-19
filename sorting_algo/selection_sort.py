arr = [5, 2, 1, 4, 3]


def selection_sort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step
        for i in range(step+1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]


selection_sort(arr)
print(arr)
