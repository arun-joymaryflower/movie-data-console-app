import csv

def load_movies(file_path):
    movies = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

def search_by_name(movies, name):
    return [movie for movie in movies if name.lower() in movie['Title'].lower()]

def search_by_year(movies, year):
    return [movie for movie in movies if movie['Year'] == year]

def search_by_director(movies, director):
    return [movie for movie in movies if director.lower() in movie['Director'].lower()]

def display_menu():
    print("1. Search movie by name")
    print("2. Search movie by release year")
    print("3. Search movie by director")
    print("4. Exit")

def main():
    movies = load_movies('movies.csv')
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter movie name: ")
            results = search_by_name(movies, name)
            print(results)
        elif choice == '2':
            year = input("Enter release year: ")
            results = search_by_year(movies, year)
            print(results)
        elif choice == '3':
            director = input("Enter director's name: ")
            results = search_by_director(movies, director)
            print(results)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
