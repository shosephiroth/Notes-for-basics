# 2D Lists & Nested Loops

# 2 Dimensional lists:

# regular list:

number_grid = [
    1, 2, 3, 4
]

# 2 Dimensional list:

number_grid2 = [
    #   columns:
    #    0  1  2
    [1, 2, 3],  # this is row 0
    [4, 5, 6],  # this is row 1
    [7, 8, 9],  # this is row 2
    [0]  # this is row 3
]

# The above is helpful because you can make grid like structures in python
# In this high level number grid list we have 4 elements, and all the elements are themselves, lists.
# This grid has 4 rows and 3 columns

# Onward to it's uses:
# Accessing individual elements inside this list structure:

# Let's say I want to print out the number 1 on that grid above.The way I can access that number is:

# put the index of the row I want to access inside square brackets. Next the column in a second pair of square brackets:

print(number_grid2[0][0])
print(number_grid2[2][1])
print(number_grid2[1][1])

print()

# Remember indexes start at 0


# Nested For loop:

# A for loop inside of a for loop. Use a Nested for loop to print out all the elements inside of an array. How to parse through a 2D list or array:

number_grid3 = [
    #   columns:
    #    0  1  2
    [1, 2, 3],  # this is row 0
    [4, 5, 6],  # this is row 1
    [7, 8, 9],  # this is row 2
    [0]  # this is row 3
]

for row in number_grid3:
    print(row)

print()

# access each of these attributes inside each of these attributes inside each of these array elements. Attributes are the numbers, array elenents are the brackets and their contents possibly?

number_grid4 = [
    #   columns:
    #    0  1  2
    [1, 2, 3],  # this is row 0
    [4, 5, 6],  # this is row 1
    [7, 8, 9],  # this is row 2
    [0]  # this is row 3
]

for row in number_grid4:
    for col in row:
        print(col)

print()