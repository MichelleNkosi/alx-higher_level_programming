#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

# The string should be exactly as shown, with the correct length
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
