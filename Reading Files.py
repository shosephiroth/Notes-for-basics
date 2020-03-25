# Reading Files

# Python read command will allow you to read files outside of your python file. .txt, .csv, .html, ect

# You can read through/parse through different files

# If files are in the same directory you can just enter the file name. Otherwise you must enter "relative path to the file" or "absolute path to the file"

open("employees.txt", "r") #file name first for the open file function, then the mode you want to open the file in. "r" stands for read. meaning you don't want to modify anything in the file

# "w" stands for write, "a" stands for append: you can add new information to the end of the file, "r+" stands for reading and writing.

# We generally want to save this open function inside a variable:

# Example:

employee_file = open("employees.txt")

# We always want to close a file too when we're done with it:

employee_file.close()

# Once you're done reading the file you can close it. Maybe too once we're done writing or appending but that's a later lesson

# There's a function inside python which helps you determine if a file is readable

print(employee_file.readable()) #This will return a boolean value: True or False

# To spit out all the information in the file:

print(employee_file.read())

# Read an individual line in a file

print(employee_file.readline()) # automatically starts with the first line
print(employee_file.readline()) # automatically moves to the 2nd line after reading the 1st

# Also, there's a better function for reading multiple lines

print(employee_file.readlines()) # This will take each line in the file and place them inside a list

# Now you can print specific lines based on their index in a list

print(employee_file.readlines()[1])

# For loop

employee_file = open("employees.txt", "r") # "r" for read
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# To add a new line to the file \n is the move. Example:

employee_file = open("employees.txt", "a") # "a" for append

employee_file.write("\nKelly - Customer Service") # this will be appended on to the end of the employee file, now with it's own line

employee_file.close()

# \n is considered an escape character

# Let's write a file. WARNING, USING "W" will overwrite the file's existing data

employee_file = open("employees.txt", "w") # w for write. This basically clears the file and replaces it with whatever you add

employee_file.write("\nKelly - Customer Service")

employee_file.close()

# You can also use "w" to create a new file.

employee_file = open("employees1.txt", "w") # new file name will create a new file instead of overwriting an existing file

employee_file.write("\nKelly - Customer Service")

employee_file.close()

# You could also write out a web page. For example:

employee_file = open("index.html", "w") # Notice the file extension name

employee_file.write("<p>This is HTML</p>") #This is where you will put the HTML

employee_file.close()