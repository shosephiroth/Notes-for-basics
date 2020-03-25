# Modules and PIP

# A module is a python file that we can import into our current python file

# all the variables, functions. and other things, and import all those things into the current file

# Written tutorial, must do this in an IDE for results, won't work in code playground

# created a python file called "useful_tools.py"

# The file reads:

import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]  # this function gets the file by name and returns it's extension


def roll_dice(num):
    return random.randint(1,
                          num)  # this function will roll a di/dice by the number you give it. Example, pass it a 6 you will get a 6 sided di


# Switching to a new file now "app.py"

# At the top of the python file, line 1 write:

import \
    useful_tools  # this will likely show up gray on the IDE. Look to line 9 for filename, this is example based real life will depend on file name

print(
    useful_tools.)  # Once you type this, your IDE will start to give you suggestions of code from that previous file. Those functions, variables, and etc will pop up

print(useful_tools.roll_dice(
    10))  # And this is how you pull a function from the file you imported. Won't work here but this is the dice rolling function from the other file

# This is really a core concept in python. Importing functionality from other python files

# You can write something once and use it whenever you want

# Google List of Python modules and choose the ones for the version you're using. This will find a lot of code that has already been written for you.

# Look for python module doing "insert what you're trying to do here" There probably is one that someone has done already

# Where are these online python modules, where are they stored?

# 2 types: Built in modules and external modules

# Lib folder under the "External Libraries" file tree in PyCharm hosts all the external modules. Lib is a very important folder

# At the top of the official python modules page, it tells you where the source of the module is

# "binascii" for example, won't list a source code because it is built into the language. "binascii - Convert between binary and ASCII"

# find the 3rd party external module you want to download/install

# pip is a program, never versions of python 3 have it automatically. pip is a package manager and allows you to install python modules.

# Open up command prompt or terminal

# to check pip installed type:

pip - -version  # typed into command prompt and possibly terminal, language might differ

# to use pip to install a module:

pip
install
python - docx

# This download package will go to the "site-packages" folder

# Check the name of the actual module once downloaded. In "python-docx" case, that was the download file name. The modules actual name is docx

# Example:

import docx

docx.  # and this is where the IDE will start to give you suggestions. Variables, functions, etc will appear from the docx python file/folder

# pip can also be used to unistall modules

# Terminal:

pip
uninstall
python - docx  # this is typed into the terminal





