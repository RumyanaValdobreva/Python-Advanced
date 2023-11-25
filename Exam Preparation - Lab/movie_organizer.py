def movie_organizer(*args):
    movies = {}
    output = ""

    for name, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(name)

    for genre, movie in sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{genre} - {len(movie)}\n"
        for mv in sorted(movie):
            output += f"* {mv}\n"

    return output