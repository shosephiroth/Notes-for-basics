movies = ["The Holy Grail", "The life of Brian", "The meaning of Life"]
print(movies[1])
print(len(movies))
movies.append("Gone with the Wind")
print(movies)
movies.pop()
print(movies)
movies.extend(["Dr. Dolittle", "American Pie", "Wedding Crashers"])
print(movies)
movies.remove("The Holy Grail")
print(movies)
movies.insert(0, "The Matrix")
print(movies)
movies.insert(1, "The Matrix Reloaded")
movies.insert(2, "The Matrix Revolutions")
print(movies)

# List exercise

#Let’s take a bit of time to try to work out which strategy to use when adding data to your list in this case.
Given the following list-creation code:

# movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# Work out the Python code required to insert the numeric year data into the preceding list, changing the list so that it ends up looking like this:

# ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

movies.clear() # clear the contents of the list

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"] # list given

# Write insertion code below:

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
print(movies)

# Now write the Python code required to re-create the list with the data you need all in one go:

movies.clear() # clear the contents of the list

movies = ['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]

# I like the first method better
