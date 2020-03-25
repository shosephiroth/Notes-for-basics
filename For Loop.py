# For Loops

# Loop through a string:

for letter in "Giraffe Academy":
    print(letter)

print()

# Loop through a list:

# this prints out the friends in the list "friends". One on each line:

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

print()

# This prints all numbers starting at 0 all the way through to and including 10:

for index in range(10):
    print(index)

print()

# With this next one, the second number specified in the range is not printed. Heads up.
# This prints out all the numbers between 3 and 10, not including 10:

for index in range(3, 10):
    print(index)

print()

# For this one below, this will give me a range from 0 to the number of friends in this list:

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(index)

print()

# Doing it this way below will allow you to access each friend in the list, same as before but this time through a range:

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])

print()

# using for loops to loop through an array is a very common function

# print something different on the first iteration of a loop. Don't be afraid to put power logic inside your loops

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
