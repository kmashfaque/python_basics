arr = [4, 2, 3, 5, 6, 1]


def max_sub_func():

    max_sub = arr[0]
    curr_sum = 0
    for n in arr:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n

        max_sub = max(curr_sum, max_sub)
    return max_sub


res = max_sub_func()
print(res)


curr_sum = 0
max_so_far = arr[0]


def max_sub_func_2(curr_sum, max_so_far):
    for i in range(len(arr)-1):
        curr_sum = curr_sum+arr[i]

        if max_so_far < curr_sum:
            max_so_far = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_so_far


res = max_sub_func_2(curr_sum, max_so_far)
print(res)
