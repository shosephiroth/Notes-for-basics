# Working with Numbers

print(2)

print()

print(2.0987)

print()

print(-2.0987) # can write out numbers in negative

print()

print(3 + 4.5) # addition

print()

print(3 - 4.5)# subtraction

print()

print(3 * 4.5) # multiplication

print()

print(3 / 4.5) # division

print()

print(3 * 4 + 5) # Python follow order of operations

print()

print(3 * (4 + 5)) # added in parenthesis for order of operations to do the addition first

print()

print(10 % 3) # Modulus operator. Read 10 mod 3. It does 10 divided by 3 and gives us the remainder which is 1

print()

# We can store these numbers inside of variables:

my_num = 5
print(my_num)

print()

# Convert numbere into a string

my_num = 5
print(str(my_num)) # will print out the same but it is now a string not a number

print()

# This is useful for when we want to print a number out with a string.

my_num= 5
print(str(my_num) + " is my favorite number")
# without str() function, we will get an error message if we try to print a number and string in the same print statement

print("\n") # is there a better practice for spacing? This is the same as print() by itself, but "\n" would be good for new lines in single print statements

# Python number functions:

# ABS meaning Absolute Value

my_num = -5
print(abs(my_num))

print()

print(pow(3, 2)) # pow stands for power. The first parameter is the base number and the second is the power/exponet to which we are raising the base number

print()

print(pow(3, 4))

print()

print(pow(4, 6))

print()
# max function tells us which of the 2 numbers is larger:

print(max(4, 6))

print()

print(max(9, 2))

print()

print(max(112, 3654))

print()

# Min function prints out the smallest number:

print(min(4, 6))

print()

print(min(9, 2))

print()

print(min(112, 3654))

print()

# Round function will round a number for you

print(round(3.2))

print()

print(round(3.4))

print()

print(round(3.5))

print()

print(round(3.7))

print()

# to access more functions may have to import more code

from math import * #this goes out and grabs a bunch of different math functions. Also known as a module. This would be the math module.

print(floor(3.7)) # floor function, rounds down no matter what. essentially just cuts off the decimal

print()

print(ceil(3.3)) # celeing function, rounds up no matter what

print()

print(sqrt(3.7)) # square root function

print()

print(sqrt(36))

print()




