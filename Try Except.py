# Try Except
# Catching errors

# Anticipate errors and handle them when they occur. That way errors don't bring our program to a crashing halt

number = int(input("Enter a number: "))
print(number)

# if you enter a non number, it will cause the program to crash. So you need to be able to handle the exceptions
# Try except block is what is used for this

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

# Specify the type of error you want to catch with this format for except:


try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")

# store error as a variable:


try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("err")
except ValueError:
    print("Invalid input")

# A best practice is to set up for catching specific errors. "Except:" by itself is too broad and may break your program on it's own