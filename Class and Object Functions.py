# Object Functions / Class Functions

# a function that we can use inside of a class it can modify the objects of that class or give us specific information about thodr objects

# Student.py file:

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


# Over on app.py file we've created 2 students:

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)


# We can create a function within the class, let's create one that determines whether or not the student is on honor roll

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):  # self always has to be the first parameter, it refers to the actual object(/student in this case)
        if self.gpa >= 3.5:  # referring to the actual student's gpa, ifi t's greater than 3.5
            return True  # boolean
        else:
            return False


# It's a small function but it provides a service to it's class by determining right there if the student is on honor roll or not.

print(student1.on_honor_roll())
print(student2.on_honor_roll())

