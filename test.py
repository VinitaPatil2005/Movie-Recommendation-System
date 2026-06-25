from app.recommend import recommend

movies = recommend("Avatar")

for movie in movies:
    print(movie)