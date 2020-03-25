# Working with strings

print("Giraffe Academy") # This prints Giraffe Academy

print() # This prints a new line

print("Giraffe\nAcademy") # \n creates a new line

print()

print("Giraffe\"Academy") # \ can also be taken literally so it allows you to add quotes in your string

print()

print("Giraffe\Academy") # Print \ in regularly

print()

# can store a string as a variable and then print it out using the variable in the print statement

phrase = "Giraffe Academy"
print(phrase)

print()

# Concatenation is the process in which you take one string and append another to it

phrase = "Giraffe Academy"
print(phrase + " is cool") # concatenation

print()

# Functions

# A block of code that we can run that will perform a specific operation for us
# Functions can modify our strings and get information

phrase = "Giraffe Academy"
print(phrase.upper()) # makes everything uppercase

print()

phrase = "Giraffe Academy"
print(phrase.lower()) # makes everything lower case

print()

phrase = "Giraffe Academy"
print(phrase.isupper()) # checks the string to see if everything is upper case

print()

phrase = "Giraffe Academy"
print(phrase.upper().isupper()) # Can use functions together, now this will read as True for the boolean because we modified the string.

print()

phrase = "Giraffe Academy"
print(len(phrase)) # This will give the length of characters in the string which is stored in the variable "phrase".

print()

# Open and closed square brackets "[]"" after phrase will target the index of the characters. Index starts at 0 then goes 1, 2 ,3, etc.

phrase = "Giraffe Academy"
print(phrase[0]) # Open and closed square brackets "[]"" after phrase will target the index of the characters. Index starts at 0 then goes 1, 2 ,3, etc.

phrase = "Giraffe Academy"
print(phrase[1])

phrase = "Giraffe Academy"
print(phrase[2])

phrase = "Giraffe Academy"
print(phrase[3])

phrase = "Giraffe Academy"
print(phrase[4])

phrase = "Giraffe Academy"
print(phrase[5])

phrase = "Giraffe Academy"
print(phrase[6])

phrase = "Giraffe Academy"
print(phrase[7])

phrase = "Giraffe Academy"
print(phrase[8])

phrase = "Giraffe Academy"
print(phrase[9])

phrase = "Giraffe Academy"
print(phrase[10])

phrase = "Giraffe Academy"
print(phrase[11])

phrase = "Giraffe Academy"
print(phrase[12])

phrase = "Giraffe Academy"
print(phrase[13])

phrase = "Giraffe Academy"
print(phrase[14])

print()

phrase = "Giraffe Academy"
# index   0123456789....  and so on but can't space double numbers appropriately

# index function will tell us where a specific character or string is located in our string

print(phrase.index("G")) # Passing a parameter/Paramter = a value that you give to a function
print(phrase.index("i"))
print(phrase.index("r"))
print(phrase.index("a"))
print(phrase.index("f"))
print(phrase.index("f"))
print(phrase.index("e"))
print(phrase.index(" "))
print(phrase.index("A"))
print(phrase.index("c"))
print(phrase.index("a"))
print(phrase.index("d"))
print(phrase.index("e"))
print(phrase.index("m"))
print(phrase.index("y"))

print()

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant")) # Can replace strings with this function

print()