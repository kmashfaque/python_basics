# A set is a collection which is unordered, unchangeable*, and unindexed.

# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# print(len(thisset))

# thisset2 = {1, 2, 3, 4, 5.5}
# print(thisset2)
# do not allow duplicate values


# It is also possible to use the set() constructor to make a set.

# thisset3 = set(("apple", "banana", "cherry"))  # note the double round-brackets
# print(thisset3)
# for x in thisset3:
#     print(x)


# Check if "banana" is present in the set:
# print("banana" in thisset3)

# adding new items
# thisset3.add("orange")
# print(thisset3)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
# mylist = ["kiwi", "orange"]
# thisset3.update(mylist)
# print(thisset3)

# removing items
# thisset3.remove("orange")
# print(thisset3)
# thisset3.discard("kiwi")
# print(thisset3)
# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
# print(thisset3.pop())

# print(thisset3.clear())

# The del keyword will delete the set completely:
# del thisset3
# print(thisset3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set1.update(set3)
print(set3)
print(set1)


# The intersection_update() method will keep only the items that are present in both sets.
set3.intersection_update(set2)
print(set3)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
set4 = set3.intersection(set2)
print(set4)


# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

y2 = x.symmetric_difference(y)
print(y2)
