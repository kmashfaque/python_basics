# command = "G()(al)"

# result = command.replace("()", "o").replace("(al)", "al")
# print(result)


# def goalparser(command):
#     d = {"G": "G", "()": "o", "(al)": "al"}
#     res = ""
#     temp = ""
#     for i in range(len(command)):
#         temp += command[i]

#         if temp in d:
#             res += d[temp]
#             temp = ""

#     return res


# result = goalparser(command)
# print(result)


# paths = [["London", "New York"], ["New York", "Lima"],
#          ["Lima", "Sao Paulo"], ["Sao Paulo", "Los angles"]]


# def destcity(paths):
#     outgoing_count = {}
#     for path in paths:
#         city_a, city_b = path

#         outgoing_count[city_a] = outgoing_count.get(city_a, 0)+1
#         outgoing_count[city_b] = outgoing_count.get(city_b, 0)

#         print(outgoing_count)
#     for city in outgoing_count:
#         if outgoing_count[city] == 0:
#             return city


# destination = destcity(paths)
# print(destination)


# increament_word = "easy2"

# temp = increament_word.split("")
# print(temp)
# k = 1


# def func(increament_word):
#     for word in temp:
#         res = ""
#         if (word.isalpha()):
#             res += word + "1"
#         elif any(char.isdigit() for char in word) and any(char.isalpha() for char in word):
#             for char in word.isdigit():
#                 print(word)
#     res += str(int((word)+k))

#     return res


# result = func(increament_word)
# print(result)

# [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]

# foo099
# foo99
# foo000


# def increament_word(string):
#     stripped_val = string.rstrip("1234567890")
#     ints = string[len(stripped_val):]
#     if len(ints) == 0:

#         return string+"1"
#     else:
#         length = len(ints)
#         ints = 1+int(ints)
#         ints = str(ints).zfill(length)
#         return stripped_val+ints


# val = increament_word("sfaxgajhxgj000")
# print(val)


# def gap(g, m, n):

#     prev_prime = n
#     for i in range(m, n+1):
#         if is_prime(i):
#             if i-prev_prime == g:
#                 return [prev_prime, i]
#             prev_prime = i
#     return None


# def is_prime(n):
#     for i in range(2, int(n**.5+1)):
#         if n % i == 0:
#             return False
#     return True
# def is_prime(n):

#     if n % 2 == 0:
#         return False
#     elif n != 3 and n % 3 == 0:
#         return False
#     elif n % 6 == 0:
#         return False
#     elif n != 5 and n % 5 == 0:
#         return False
#     elif n % 3 == 0 and n % 5 == 0:
#         return False
#     elif n % 3 == 0 and n % 7 == 0:
#         return False
#     elif n != 7 and n % 7 == 0:
#         return False
#     elif n % 9 == 0:
#         return False
#     return True


# val = gap(2, 3, 50)
# print(val)

# counting the smaller values from the current element
arr1 = [1, 8, 2, 2, 3]
# #
arr2 = []
# count = 0

# for i in arr1:
#     count = 0
#     for j in arr1:
#         if i > j:
#             count += 1

#     arr2.append(count)

# print(arr2)

# smaller_count = {}
# sorted_arr = sorted(arr1, reverse=True)

# for i in range(len(sorted_arr)-1):

#     curr_val = sorted_arr[i]
#     next_val = sorted_arr[i+1]
#     if next_val < curr_val:
#         count = len(sorted_arr)-(i+1)
#         smaller_count[curr_val] = count
#     smaller_count[sorted_arr[-1]] = 0

# for nums in arr1:
#     arr2.append(smaller_count[nums])

# print(arr2)


# two_sum = [1, 3, 2, 4, 10, 8]
# target = 9
# prev_hash = {}


# def Two_sum(two_sum):
#     for i, n in enumerate(two_sum):
#         diff = target-n
#         if diff in prev_hash:
#             return [prev_hash[diff], i]
#         prev_hash[n] = i
#     return


# res = Two_sum(two_sum)
# print(res)

# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []

# while my_list:
#     min = my_list[0]
#     for x in my_list:
#         if x < min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)

# print(new_list)


# def fibonacci_num(n):
#     num_1 = 0
#     num_2 = 1
#     sums = 0
#     for i in range(1, n+1):
#         print(num_1)
#         sums = num_1+num_2
#         num_2 = num_1
#         num_1 = sums


# fibonacci_num(9)


# def powerOfTwo(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power*2
#         i += 1
#     return power


# val = powerOfTwo(3)
# print(val)


# def recursion(n):

#     if n == 1 or n == 0:
#         return 1
#     else:

#         power = n*recursion(n-1)

#         return power


# val = recursion(0)
# print(val)


# def func(n):
#     result = 1
#     if n == 0 or n == 1:
#         return 1
#     for i in range(1, n+1):

#         result = result*i
#     return result


# val = func(5)
# print(val)
