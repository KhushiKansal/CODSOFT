# Movie recommendation

class Movie:
    def _init_(self, title, genres):
        self.title = title
        self.genres = genres

def recommend_similar_movies(movie_title, movies, num_recommendations=5):
    recommended_movies = []
    
    # Find the movie object with the given title
    target_movie = None
    for movie in movies:
        if movie.title.lower() == movie_title.lower():
            target_movie = movie
            break
    
    if target_movie is None:
        print("Movie not found!")
        return recommended_movies

    target_genres = set(target_movie.genres)

    for movie in movies:
        # Skip the target movie itself
        if movie.title.lower() == movie_title.lower():
            continue
        
        # Check if any genre of the movie matches with genres of the target movie
        if any(genre in target_genres for genre in movie.genres):
            recommended_movies.append(movie)

    # Sort recommended movies based on the number of matched genres
    recommended_movies.sort(key=lambda x: len(set(x.genres).intersection(target_genres)), reverse=True)

    return recommended_movies[:num_recommendations]

# Sample movies
movies = [
    Movie("The Shawshank Redemption", ["Drama"]),
    Movie("The Godfather", ["Crime", "Drama"]),
    Movie("The Dark Knight", ["Action", "Crime", "Drama"]),
    Movie("Forrest Gump", ["Drama", "Romance"]),
    Movie("Inception", ["Action", "Adventure", "Sci-Fi"]),
    Movie("Pulp Fiction", ["Crime", "Drama"]),
    Movie("The Shawshank Redemption", ["Drama"]),
    Movie("The Godfather", ["Crime", "Drama"]),
    Movie("The Dark Knight", ["Action", "Crime", "Drama", "Thriller"]),
    Movie("Forrest Gump", ["Drama", "Romance"]),
    Movie("Inception", ["Action", "Adventure", "Sci-Fi", "Thriller"]),
    Movie("Pulp Fiction", ["Crime", "Drama"]),
    Movie("The Matrix", ["Action", "Sci-Fi"]),
    Movie("Schindler's List", ["Biography", "Drama", "History"]),
    Movie("The Lord of the Rings: The Return of the King", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("The Silence of the Lambs", ["Crime", "Drama", "Thriller"]),
    Movie("Fight Club", ["Drama"]),
    Movie("Star Wars: Episode V - The Empire Strikes Back", ["Action", "Adventure", "Fantasy", "Sci-Fi"]),
    Movie("Forrest Gump", ["Drama", "Romance"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("The Lord of the Rings: The Two Towers", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("Goodfellas", ["Biography", "Crime", "Drama"]),
    Movie("The Usual Suspects", ["Crime", "Drama", "Mystery", "Thriller"]),
    Movie("Se7en", ["Crime", "Drama", "Mystery", "Thriller"]),
    Movie("The Shawshank Redemption", ["Drama"]),
    Movie("The Godfather: Part II", ["Crime", "Drama"]),
    Movie("The Green Mile", ["Crime", "Drama", "Fantasy", "Mystery"]),
    Movie("The Prestige", ["Drama", "Mystery", "Sci-Fi", "Thriller"]),
    Movie("The Departed", ["Crime", "Drama", "Thriller"]),
    Movie("Gladiator", ["Action", "Adventure", "Drama"]),
    Movie("The Lion King", ["Animation", "Adventure", "Drama", "Family", "Musical"]),
    Movie("Interstellar", ["Adventure", "Drama", "Sci-Fi"]),
    Movie("Saving Private Ryan", ["Drama", "War"]),
    Movie("The Sixth Sense", ["Drama", "Mystery", "Thriller"]),
    Movie("Titanic", ["Drama", "Romance"]),
    Movie("Inglourious Basterds", ["Adventure", "Drama", "War"]),
    Movie("The Pianist", ["Biography", "Drama", "Music", "War"]),
    Movie("The Godfather: Part III", ["Crime", "Drama"]),
    Movie("The Truman Show", ["Comedy", "Drama", "Sci-Fi"]),
    Movie("The Big Lebowski", ["Comedy", "Crime", "Sport"]),
    Movie("Memento", ["Mystery", "Thriller"]),
    Movie("Jurassic Park", ["Action", "Adventure", "Sci-Fi", "Thriller"]),
    Movie("Catch Me If You Can", ["Biography", "Crime", "Drama"]),
    Movie("A Beautiful Mind", ["Biography", "Drama"]),
    Movie("The Grand Budapest Hotel", ["Adventure", "Comedy", "Crime"]),
    Movie("Gone with the Wind", ["Drama", "History", "Romance"]),
    Movie("The Wizard of Oz", ["Adventure", "Family", "Fantasy", "Musical"]),
    Movie("Braveheart", ["Biography", "Drama", "History", "War"]),
    Movie("The Revenant", ["Action", "Adventure", "Biography", "Drama", "Western"]),
    Movie("The Shining", ["Drama", "Horror"]),
    Movie("The Godfather: Part III", ["Crime", "Drama"]),
    Movie("Back to the Future", ["Adventure", "Comedy", "Sci-Fi"]),
    Movie("Schindler's List", ["Biography", "Drama", "History"]),
    Movie("The Silence of the Lambs", ["Crime", "Drama", "Thriller"]),
    Movie("The Terminator", ["Action", "Sci-Fi"]),
    Movie("Casablanca", ["Drama", "Romance", "War"]),
    Movie("The Departed", ["Crime", "Drama", "Thriller"]),
    Movie("Avatar", ["Action", "Adventure", "Fantasy", "Sci-Fi"]),
    Movie("WALL·E", ["Animation", "Adventure", "Family", "Sci-Fi"]),
    Movie("The Intouchables", ["Biography", "Comedy", "Drama"]),
    Movie("The Prestige", ["Drama", "Mystery", "Sci-Fi", "Thriller"]),
    Movie("Alien", ["Horror", "Sci-Fi"]),
    Movie("Django Unchained", ["Drama", "Western"]),
    Movie("Indiana Jones and the Raiders of the Lost Ark", ["Action", "Adventure"]),
    Movie("The Lion King", ["Animation", "Adventure", "Drama", "Family", "Musical"]),
    Movie("Monty Python and the Holy Grail", ["Adventure", "Comedy", "Fantasy"]),
    Movie("Finding Nemo", ["Animation", "Adventure", "Comedy", "Family"]),
    Movie("The Shawshank Redemption", ["Drama"]),
    Movie("The Godfather: Part II", ["Crime", "Drama"]),
    Movie("The Dark Knight", ["Action", "Crime", "Drama", "Thriller"]),
    Movie("12 Angry Men", ["Crime", "Drama"]),
    Movie("Schindler's List", ["Biography", "Drama", "History"]),
    Movie("The Lord of the Rings: The Return of the King", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("Pulp Fiction", ["Crime", "Drama"]),
    Movie("The Good, the Bad and the Ugly", ["Western"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("Fight Club", ["Drama"]),
    Movie("Forrest Gump", ["Drama", "Romance"]),
    Movie("Star Wars: Episode V - The Empire Strikes Back", ["Action", "Adventure", "Fantasy", "Sci-Fi"]),
    Movie("Inception", ["Action", "Adventure", "Sci-Fi", "Thriller"]),
    Movie("The Lord of the Rings: The Two Towers", ["Action", "Adventure", "Drama", "Fantasy"]),
    Movie("The Matrix", ["Action", "Sci-Fi"]),
    Movie("Goodfellas", ["Biography", "Crime", "Drama"]),
    Movie("One Flew Over the Cuckoo's Nest", ["Drama"]),

]

# Input movie title from the user
input_movie = input("Enter a movie title: ")

# Get recommendations for the input movie
recommendations = recommend_similar_movies(input_movie, movies)

# Print recommendations
if recommendations:
    print("\nRecommendations for movies similar to", input_movie + ":")
    for movie in recommendations:
        print(movie.title)
else:
    print("No recommendations found.")