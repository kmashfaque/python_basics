# multiple loop
# colors=["yellow","green","blue","red"]
# fruits=["apple","mango","orange"]

# for x in colors:
#     for y in fruits:
#         print(x,y)


# iterate through the index
# colors2 = ["yellow", "green", "blue", "red"]
# for index, color in enumerate(colors2):
# print(f" COLOR: {color} index is {index}")


# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# newlists[]

# for x in numbers:
#     newlists.append(x**2)

# print(newlists)


# import random
# n = 20
# to_be_guessed = int(n*random.random())+1
# print(to_be_guessed)
# guess = 0

# while guess != to_be_guessed:
#     guess = int(input("New number: "))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print("The number is too large")
#         elif guess < to_be_guessed:
#             print("Number is too small")
#     else:
#         print("Sorry you have given up")
#         break
# else:
#     print("You have guessed the current number")


# n = int(input("put your number: "))
# result = 1

# if n < 0:
#     print("the number provided must be positive")
# elif n == 0:
#     result = 1
# else:
#     for x in range(1, n+1):
#         result = result*x

# print(result)

# from math import sqrt
# n = int(input("Enter the maximal number: "))

# for a in range(1, n+1):

#     for b in range(a, n+1):

#         c_square = a**2 + b**2

#         c = int(sqrt(c_square))
#         if((c_square-c**2) == 0):
#             print(a, b, c)

# def fibonacchi(n_term):
#     num = 0
#     num1 = 1
#     count = 0
#     while count < n_term:
#         print(num)
#         temp = num1
#         num1 = num+num1
#         num = temp
#         count = count+1

# n_term = int(input("Enter your number: "))

# fibonacchi(n_term)

# newarr1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# newarr2 = [
#     [10, 11, 12],
#     [13, 14, 15],
#     [16, 17, 18],
# ]

# result = []

# for x in range(len(newarr1)):
#     for y in range(len(newarr1[x])):
#         result.append(newarr1[x][y]+newarr2[x][y])
# print(result)


travelling = input("Do you want to travel?? ")


while travelling == "yes":
    num = int(input("number of people travelling: "))
    for num in range(1, num+1):
        name = input("Name: ")
        age = input("Age: ")
        sex = input("Male or Female: ")

        print(name)
        print(age)
        print(sex)
    travelling = input("Oops! forgot someone: ")
