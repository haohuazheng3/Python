from movies import Movies

def display_menu():
    print("------ Menu ------")
    print("q - Quit")
    #Add more menu options here if necessary in the future

def main():
    movies = Movies('./movies.txt')

    while True:
        display_menu()

        option = input("Choose an option: ")

        if option == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    