# Building a Basic Calculator

# We'll get 2 numbers from a user and then add those numbers together

#Let's create 2 variables and then get 2 numbers that the user wants to add together:

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# Then let's create a variable to store the result:
result = num1 + num2
# Next we print the variable that holds the result:
print(result)

# The result is 5152 because right now the variables are stored as strings, we must convert them to integers. Here's how the code will look the correct way:

result2 = int(num1) + int(num2) #this would be in place of line 10
print(result2) # in place of line 12