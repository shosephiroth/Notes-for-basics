
fav_movies = ["The Holy Grail", "The Life of Brian"]

print(fav_movies[0])
print(fav_movies[1])

#iteration example:

# for loop:
# The keyword “for” indicates the start of the loop and comes before the target identifier.
# The keyword “in” separates the target identifier from your list.
# for i in list; i is commonly used as a variable/target identifier

for each_flick in fav_movies:
    print(each_flick)

# while loop:

# When you use “while”, you have to worry about “state information,” which requires you to employ a counting identifier

count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1

# When you use “for”, the Python interpreter worries about the “state information” for you.

for each_item in movies:
    print(each_item)
    
