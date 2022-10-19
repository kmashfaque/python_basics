# car = {
# "brand": "rolls royes",
# "production": 1990,
# "color": "black",

# }

# print(car["brand"])

# car["brand"] = "BMW"
# print(car["brand"])

# print(car.get("production"))
# print(car.keys())
# print(car.values())
# print(car.items())

# if "brand" in car:
#     print("Yes, model is in this dictionary")
# else:
#     print("Oops! Not in the dictionary!!")

# car.update({"brand": "porche"})
# print(car["brand"])

# print(car)

# remove item
# car.pop("brand")
# print(car)
# print(car.popitem())
# print(car)


# del car
# print(car)

# car.clear()
# print(car)


# loop in dict

# this will loop through the keys of dict
# for x in car:
#     print(x)
# for x in car.keys():
#     print(x)

# this will print the values of the dict

# for x in car:
#     print(car[x])

# for x in car.values():
#     print(x)


# looping through both keys and values by using items() method:
# for x, y in car.items():
#     print(f"{x.upper()}: {y}")


# copying the dictionary
# car1 = car.copy()
# print(car1)
# car2 = dict(car1)
# print(car2)


# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(myfamily["child1"]["name"])


# dictionary methods
# get()
# pop()
# popitem()
# del
# clear()
# keys()
# values()
# items()
# update()


# phone = input("Phone: ")

# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""

# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)


# emoji converter
msg = input(">")
words = msg.split(" ")

emojis = {
    ":)": "🙂",
    "sad": "😌"
}

output = ""
for word in words:
    output += emojis.get(word, word)+" "
print(output)
