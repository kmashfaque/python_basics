# arr = [-4, 3, 3, -3, 4, -1]


# def max_sub_func():

#     max_sub = arr[0]
#     curr_sum = 0
#     for n in arr:
#         if curr_sum < 0:
#             curr_sum = 0
#         curr_sum += n

#         max_sub = max(curr_sum, max_sub)
#     return max_sub


# res = max_sub_func()
# print(res)


# curr_sum = 0
# max_so_far = arr[0]


# def max_sub_func_2(curr_sum, max_so_far):
#     for i in range(len(arr)-1):
#         curr_sum = curr_sum+arr[i]

#         if max_so_far < curr_sum:
#             max_so_far = curr_sum
#         if curr_sum < 0:
#             curr_sum = 0
#     return max_so_far


# res = max_sub_func_2(curr_sum, max_so_far)
# print(res)


# arr = [-4, 3, 3, -3, 4, -1]

# max_sub = arr[0]
# cuur_sum = 0
# for n in arr:
#     if cuur_sum < 0:
#         cuur_sum = 0
#     cuur_sum += n
#     print("curr sum: ", cuur_sum)
#     max_sub = max(max_sub, cuur_sum)
#     print("max_sub:", max_sub)


# arr = [-4, 3, 3, -3, 4, -1]

# curr_sum = 0
# max_sum = arr[0]
# for i in range(len(arr)-1):
#     for j in range(i, len(arr)):
#         curr_sum = curr_sum+arr[j]
#         max_sum = max(curr_sum, max_sum)
#     curr_sum = 0

# print(max_sum)


# string = "AAABCADDE"


# def merge_tools(string, k):
#     while string:
#         seen = ""
#         s = string[0:k]

#         for c in s:
#             if c not in seen:
#                 seen += c

#         print(seen)
#         string = string[k:]


# merge_tools(string, 3)
import collections
from collections import Counter

string = "eeaaabbbbcceedd"

hash_map = {}

for s in sorted(string):
    if s not in hash_map:
        hash_map[s] = 1
    else:
        hash_map[s] += 1

# for w in sorted(hash_map, key=hash_map.get, reverse=True):

# print(w, hash_map[w])
z = Counter(hash_map).most_common(3)

for x in z:
    print(*x)
