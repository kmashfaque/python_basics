# file = open("test.txt", "r")
# this will print first 100 word from the file
# print(file.read(100))

# file.close()


# this loop will print every line one by one in the file
# for each_line in file:
#     print(each_line, end="")


# using the content manager
# with open("test.txt", "r") as file:
# for lines in file:
#     print(lines,end="")
# file_contents = file.readline()
# print(file_contents)


# with open("test.txt", "r") as file:
# size_to_read = 10
# file_contents = file.read(size_to_read)
# print(file_contents, end="")

# file.seek(00)

# file_contents = file.read(size_to_read)
# print(file_contents)

# print(file.tell())

# while len(file_contents) > 0:
#     print(file_contents, end="")
#     file_contents = file.read(size_to_read)


# with open("test.txt", "r") as file_read:
#     with open("test_copy.txt", "w") as file_write:
#         for line in file_read:
#             file_write.write(line)
