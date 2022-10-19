# name =input("Enter your name: ")

# print("hello",name)

# tripple equals for multiple lines
# message="""hello abir's
# cartoon in the 1990"""
# print(len(message))

# variable="hello"

# print(variable[0:3])
# print(variable[:3])
# print(variable[0:])
# print(variable[-5:-2])
# print(variable.upper())


# x="12"
# y="who"

# print(type(int(x)))
# print(type(y))


# camelCase
# myVariableName = "John"

# pascal case
# MyVariableName = "John"

# snake case
# my_variable_name = "John"


# assigning multiple variables

# fruit1,fruit2,fruit3="banana","orange","apple"
# print(fruit1)
# print(fruit2)
# print(fruit3)

# fruit4=fruit5=fruit6="banana"

# print(fruit4)
# print(fruit5)
# print(fruit6)


# fruits=["banana","orange","apple"]

# fruit7,fruit8,fruit9=fruits

# print(fruit7)
# print(fruit8)
# print(fruit9)
# print(fruits[0])


# newvariable="hello, world"

# print(newvariable.strip())
# print(newvariable.split(","))
# print(newvariable.strip().replace("h","j"))

# we cannot concate strings and numbers like this
# age=24
# message="My name is john. I am "+age+"years old"
# print(message)

# we can concate by the following methods
# age=24
# message="My name is john. I am {} years old"
# print(message.format(age))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity,itemno,price))


# or by this
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {0} pieces of item {1} for {2} dollars."
# print(myorder.format(quantity,itemno,price))


# escape characters
# txt = "we are the so called \"VIKINGS\" from the north"
# print(txt)


# lists

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# thislist = ["apple", "mango", "banana", "cherry", "watermalon"]
# print(thislist)
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist[1:2] = ["orange", "kiwi"]
# print(thislist)

# adding list item to the specified index
# thislist.insert(1, "mango")
# print(thislist)

# adding to the last
# thislist.append("litchi")
# print(thislist)
# tropical = ["pinaple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# removing from lists
# thislist.remove("pinaple")
# print(thislist)
# thislist.pop()
# print(thislist)
# del thislist[0]
# print(thislist)
# del thislist
# print(thislist)
# thislist.clear()
# print(thislist)

# copying the list
# mylist = thislist.copy()
# print(mylist)
# mylist2 = list(thislist)
# print(mylist2)

# joining two list
# mylist3 = mylist+mylist2
# print(mylist3)
# mylist3.extend(mylist3)
# print(len(mylist3))


# lists or array methods
# append()
# copy()
# clear()
# remove()
# pop()
# count()
# insert()
# reverse()
# sort()
# extend()
# delete()


# my_list = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# mx = my_list[0]

# for number in my_list:
#     if number > mx:
#         mx = number
# print(mx)


# numbers2 = [2, 2, 3, 3, 4, 5, 6, 7, 5, 4, 7, 7]
# uniques = []

# for number in numbers2:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


# removing sufffix prefix
# my_string = "   xxpythonyyyy   "
# my_string = my_string.strip()
# my_string = my_string.removeprefix("xx")
# my_string = my_string.removesuffix("yyyy")
# print(my_string)
