# Classes and Objects

# Extremely important in python. Can help make your programs more powerful and organized

# There aren't always things that can be represented using strings numbers or booleans

# A phone, a computer, a person. How could they be represented?

# The data types that we have available to us in python can't cover these things

# So with classes and objects we can essentially create our own data types.


# create my own data type for anything I want. For example creating a phone data type I can store all the information I would want to know about a phone for that data type.

# So we could create a class

# A class is used to define your own data type. They are used in almost every single major programming language out there

# Let's say we're making a program for a college or university and we want to store student information

# Well we don't have a student data type. So we create a class

# Make a new python file called student.py

# example:

class Student:
    def__init__(
        self):  # this is an initialized function. Two underscores on each side of "init". I can map out what attributes a student should have with this function


# Example:

class Student:

    def __init__(self, name, major, gpa,
                 is_on_probation):  # with this function we are defining what a student is. This is a student data type we've created
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# So now we've created the template. So now we can create an actual student which is called an object. Classes are what define objects essentially.

# Now switching python files, going back to app.py

from Student import \
    Student  # What this is saying is that from the student file, we want to import the student class. Even though they share the name Student the 1st is file 2nd is class

#    file           class

student1 = Student("Jim", "Business", 3.1, False)
# variable/class          object  name,  major,    gpa,  is_on_probation

print(student1.name)  # will print out student's name

print(student.gpa)  # will print out student's gpa

# Example of another student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)


# More on explaining the class and object functions

class Student:

    def __init__(self, name, major, gpa, is_on_probation):  # creating students in the other file pass in to these assigned parameters. When we create the student we're calling that function
        self.name = name  # object.name is equal to name value we passed in/parameter above. That's what this line of code means. "Self.name" is an attribute of student
        self.major = major  # object.major is equal to major value we passed in/parameter above
        self.gpa = gpa  # object.gpa is equal to gpa value we passed in/parameter above
        self.is_on_probation = is_on_probation  # you get it, reminder this is a boolean

# When you create a student you call the function and give the information to the object to store as it's attributes

# Now you can model any real life thing by giving it attributes. Can also make imaginary things, used for making gamees if I want.

# Make monster game


