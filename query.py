from movies import Movies

movies = Movies('movies.txt')

def display_menu():
    print("Menu:")
    print("1. List all movie names")
    print("2. Search the movie name")
    print("3. Search movies by cast")
    print("q. Quit")
    return input("Please select an option: ")

def list_all_movie_names():
    movie_names = movies.get_all_movie_names()
    if movie_names:
        print("\nAll Movies:")
        for name in movie_names:
            print(name)
        print("\n")
    else:
        print("\nNo movies found.\n")

def search_movie_by_name():
    keyword = input("Enter the word to search for in movie names: ")
    results = movies.search_movies_by_name(keyword)
    if results:
        print("\n".join(results))
    else:
        print("No movies found with the specified word.")

def search_movie_by_cast():
    keyword = input("Enter the word to search for in movie casts: ")
    results = movies.search_movies_by_cast(keyword)
    if results:
        for movie in results:
            print(movie['name'])
            print(movie['cast'])
    else:
        print("No movies found with the specified word in the casts.")


if __name__ == "__main__":
    while True:
        choice = display_menu()
        if choice == 'q':
            break
        elif choice == '1':
            list_all_movie_names()
        elif choice == '2': 
            search_movie_by_name()
        elif choice == '3': 
            search_movie_by_cast()
        else:
            print("\nInvalid option. Please try again.\n")
