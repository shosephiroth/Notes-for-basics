# Build a translator:

# We'll be able to take in a string or word and translate it into a different language

# Giraffe Language:
# vowels -> g
#------------------

# dog -> dgg
# cat -> cgt

def translate(phrase):
    translation =""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print()

# created using a for loop in combination with an if statement

# The code below works too just another variant/way of writing it. Line 15 vs Line 32

def translate(phrase):
    translation =""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print()

# example below makes it so that lower case and upper case are both covered should they come across the function
def translate(phrase):
    translation =""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print()