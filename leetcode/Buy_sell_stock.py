arr = [2, 1, 3, 9, 8, 4, 5, 6, 7]


def best_sell():
    l, r = 0, 1
    maxP = 0

    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r]-arr[l]
            # print(profit)
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP


res = best_sell()
print(res)
