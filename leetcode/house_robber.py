arr = [8, 9, 1, 7]


def robbing():
    l, r = 0, 0

    for n in arr:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        temp = max(n+l, r)

        l = r
        r = temp
    return r


# robbing()
result = robbing()
print(result)
