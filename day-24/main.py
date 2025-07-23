# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#same thing as code up top but automatically closes the file
with open("../../Desktop/my_file.txt") as file: #file can be any name
     contents = file.read()
     print(contents)

# ../Desktop/my_file.txt

# mode = "w" is writing a file, but it replaces everything
# mode = "a" is appending a file, so it doesn't replace everything
# with open("my_file.txt", mode="w") as file: #file can be any name
#     file.write("\nNew Text.")

# if you try to write to a non-existing file, it will create a new one for you
# with open("new_file.txt", mode="w") as file: #file can be any name
#     file.write("\nNew Text.")