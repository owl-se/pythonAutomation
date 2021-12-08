movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("What film have you seen: ")

if user_movie in movies_watched:
    print(f"I've wathced {user_movie} too!")
else:
    print("I haven't watched yet")
