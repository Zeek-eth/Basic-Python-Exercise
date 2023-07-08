# create an application that has a list of dictionaries
movie_0 = {"name": "Casablanca", "year": 1942}
movie_1 = {"name": "Forest Gump", "year": 1994}
movie_2 = {"name": "Old Guard", "year": 2019}
movie_3 = {"name": "Race", "year": 2010}
movie_4 = {"name": "Cruiser", "year": 2015}
movie_5 = {"name": "Don", "year": 1992}

# Movie list contains all the movies
movies = [movie_0, movie_1, movie_2, movie_3, movie_4, movie_5]

# empty list for old movies and new movies
new_movie = []
old_movie = []

# loop through all the movies
for move in movies:
    name = move["name"]
    year = move["year"]

    # here comes the if statements to append
    if year > 2000:
        new_movie.append(name)
    else:
        old_movie.append(name)

# print the message on separate lines
# sort out the movies with respect to 2000
text = "\n".join(new_movie)
test = "\n".join(old_movie)
print(f"These movies has been released in the year 2000 or later:\n{text}")
print(f"These movies has been released before the year 2000:\n{test}")

