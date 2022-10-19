# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple)
# print(thistuple[2:5])
# print(thistuple[:4])


# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# update tuple

# convert the tuples to list be able to change it
# y = list(thistuple)
# y[1] = "kiwi"
# y.append("litchi")
# thistuple = tuple(y)
# print(thistuple)

# y = ("orange",)
# thistuple += y
# print(thistuple)


# unpacking tuples
# fruits = ("apple", "mango", "banana",)
# green, yellow, blue = fruits
# print(green)
# print(yellow)
# print(blue)

# fruits = ("apple", "banana", "cherry", "strawbery", "raspberry")
# (yellow, green, *blue) = fruits
# print(green)
# print(yellow)
# print(blue)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)


# join tuples
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits*2
# print(mytuple)
# tuple3 = fruits+mytuple
# print(tuple3)
