
# fact_number = int(input("Type your number: "))


# def factorial():
#     result = 1
#     for i in range(1, fact_number+1):
#         if fact_number < 0:
#             return 0
#         result *= i
#     return result


# print(factorial())


# items = [1, 2, 3, 4, 5, 6, 7, 89]


# max_number = items[0]
# for number in items:

#     if number > max_number:
#         max_number = number
# print(max_number)

# def fun(variable):
#     vowels = ["a", "e", "i", "o", "u"]
#     if variable in vowels:
#         return True
#     else:
#         return False


# sequence = "My name is abeer"
# result = filter(fun, sequence)

# for word in result:
#     print(word)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 22, 223, 222]


# def checking_func(numbers):
#     if numbers % 2 == 0:
#         return numbers


# result2 = filter(checking_func, numbers)

# for number in result2:
#     print(number)


# i = 0
# name = "geeksforgeeks"

# while i < len(name):
#     if name[i] == "e" or name[i] == "g":
#         i += 1
#         continue
#     print(name[i])
#     i += 1


# j = 0
# name2 = "geeksforgeeks"

# while j < len(name2):
#     if name2[j] == "e":
#         j += 1
#         break
#     print(name2[j])
#     j += 1

# i = 0

# while i < 4:
#     i += 1
#     print(i)
#     break
# else: #not executed because of break statement
#     print("No break")


# i = 0

# while i < 4:
#     i += 1
#     print(i)
# else:  # excuted because no break statement
#     print("No break")


# finding the intersection between the list items
# arr2 = [1, 2, 3, 4, 5]
# arr1 = [1, 2]

# result = []
# for x in arr1:
#     if x in arr2:
#         result.append(x)


# print(result)

# result = list(filter(lambda x: x in arr1, arr2))

# print(result)


# program for third largest number
my_List = [[3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5]]

# sorting every sublist of the above list


def sort_List(num): return (sorted(n) for n in num)


def third_largest(x, func): return [l[len(l)-2] for l in func(x)]


print(list(third_largest(my_List, sort_List)))
