nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []

# for n in nums:
#     my_list.append(n)
# print(my_list)


# my_list_1 = [n for n in nums]
# print(my_list_1)

# my_list_2 = [n*n for n in nums]
# print(my_list_2)


# def mul(i):
#     return i*i


# x = map(mul, nums)
# print(list(x))


# using lambda functin with map
# resu = map(lambda i: i+1, nums)
# print(list(resu))

# str_1 = "Hello from the python map"


# def upper_function(n):
#     return n.upper()


# resu_1 = map(upper_function, str_1)
# print(list(resu_1))


# car_dict = {'a': 'Mercedes-Benz', 'b': 'BMW',
#             'c': 'Ferrari', 'd': 'Lamborghini', 'e': 'Jeep'}

# car_dict_1 = map(lambda x: (x[0], x[1]+"_"), car_dict.items())
# print(dict(car_dict_1))
# x = car_dict.items()

# print(len(car_dict))


# for x, y in car_dict.items():
#     print(x, y)


# even_nums = []

# for x in nums:
#     if x % 2 == 0:
#         even_nums.append(x)
# print(even_nums)


# even_nums_2 = [x for x in nums if x % 2 == 0]
# print(even_nums_2)


# filter function

# def fun(variables):
#     letters = ["a", "e", "i", "o", "u"]
#     if variables in letters:
#         return True
#     else:
#         return False


# sequence = ['g', "e", "e", "k", "s"]

# filtered = filter(fun, sequence)
# print(tuple(filtered))
# print("The filtered words are: ")
# for words in filtered:
#     print(words)


# letter and number pair
# my_list = []
# for letter in "abcd":
#     for num in range(1, 5):
#         my_list.append((letter, num))
# print(my_list)


# dictionary comprehension


country = ['Bangladesh', "Pakistan", "Srilanka"]
capital = ['Dhaka', "Karachi", "Kolombo"]

# print(tuple(zip(country, capital)))
# dic_1 = {}

# for key, value in zip(country, capital):
#     dic_1[key] = value

# print(dic_1)


# dictionary comprehension
# dict_using_comp = {key: value for (key, value) in zip(country, capital)}

# print("Output Dictionary using dictionary comprehensions:", dict_using_comp)


# generator comprehension
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

# output_gen = (var for var in input_list if var % 2 == 0)

# print("Output values using generator comprehensions:", list(output_gen))

# for var in output_gen:
#     print(var)
