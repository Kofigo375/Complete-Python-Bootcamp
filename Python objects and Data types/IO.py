myfile = open("myfile.txt")
# # the read() method : returns the whole file as a single string
# # the readlines() : returns a list of all the lines in the text.

print(myfile.read())
print(myfile.readlines())


# best practice for opening files

with open("myfile.txt") as myfile:
    file_content = myfile.read()

# the mode: argument in the open method can be used to give
# permissions. mode = 'r' for reading.. mode = 'w' for writing etc

with open("created.txt", mode='w') as f:
    f.write("I created this random file!")

with open("created.txt", mode='r') as f:
    print(f.read())

