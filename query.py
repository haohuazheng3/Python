from movies import Movies

movies = Movies('movies.txt')

def display_menu():
    print("Menu:")
    print("1. List all movie names")
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

if __name__ == "__main__":
    while True:
        choice = display_menu()
        if choice == 'q':
            break
        elif choice == '1':
            list_all_movie_names()
        else:
            print("\nInvalid option. Please try again.\n")
