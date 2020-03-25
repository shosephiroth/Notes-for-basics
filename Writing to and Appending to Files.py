# Writing to and appending to Files

# Reading the file:

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# This is more of a readme for how to do these functions since I cannot open, read, and/or write and append files on sololearn.

employee_file = open("employees.txt", "a") #reminder a stands for append, r for read, w for write, r+ for read

employee_file.write("Toby - Human Resources") #This will add this person and job title on the end of the file

employee_file.close()

# You must be careful when writing files you can mess ip a file