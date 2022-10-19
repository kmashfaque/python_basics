# iterator is an object that contains a countable number of values
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# mystr = "banana"
# myit1 = iter(mystr)

# print(next(myit1))
# print(next(myit1))
# print(next(myit1))
# print(next(myit1))
# print(next(myit1))
# print(next(myit1))


class Numbers:
    def __iter__(self):
        self.a = 1
        print(self.__dict__)
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = Numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
