# Inheritance

# app.py:

from Chef import Chef

myChef = Chef()


# Meanwhile in Chef.py:

class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a special dish")


# Back to app.py

from Chef import Chef

myChef = Chef()
myChef.make_special_dish()


# Let's say we want to make a new type of chef

# New file created called AdvancedChef.py:

class AdvancedChef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")


# Back to app.py:

from Chef import Chef
from AdvancedChef import AdvancedChef

myChef = Chef()
myChef.make_special_dish()

myAdvancedChef = AdvancedChef()
myAdvancedChef.make_special_dish()

# This is where Inheritance comes in. Instead of having to copy and paste lines 13-20 to 35-42 to get the Advanced Chef to do the same and more than the Chef; you can use Inheritance:


from Chef import Chef


class AdvancedChef(
    Chef):  # placing a class inside the parenthesis of this new class allows the new class to inherit the attributes of the class placed in parenthesis.

    def make_fried_rice(
            self):  # additional function that "Chef" does not have. "Advanced Chef" inherited all of "Chef's" functions and has one of it's own.
        print("The chef makes fried rice")

    def make_special_dish(
            self):  # because of inheritance this would normally be "print("The chef makes a special dish")" but you can override Inheritance by writing line over in function
        print("The chef makes orange chicken")