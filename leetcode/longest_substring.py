string = "adbadcadefg"


def again():

    charSet = set()
    l = 0
    res = 0

    for r in range(len(string)):

        while string[r] in charSet:

            charSet.remove(string[l])

            print(charSet)
            l += 1

        charSet.add(string[r])
        res = max(res, r-l+1)
    return res


val = again()


# print(val)
# def without_repeat():
#     d = {}

#     res = 0
#     l = 0
#     for i in range(0, len(string)):
#         if string[i] in d:
#             l = max((d[string[i]]+1), l)
#         res = max(res, (i-l+1))
#         d[string[i]] = i
#         print(d)

#     return res


# val = without_repeat()
# print(val)
