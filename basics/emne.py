# items = ["a", "b", "c", "d", "e", "a", "a", "b", "d"]

# k = {}
# for i in items:
#     print(k)
#     if i in k:

#         k[i] += 1

#     else:
#         k[i] = 1
# print(k)


# new = {
#     "a": "one",
#     "b": "two"
# }
new = ["a", "b"]

k = {}

for i in new:
    if i in k:
        k[i] += 1
    else:
        k[i] = 1
print(k)
