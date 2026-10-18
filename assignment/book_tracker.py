import csv


def dashboard():
    """Prints
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    print('=' * 40)
    print('  📚  YOUR LIBRARY')
    print('=' * 40)


def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour.
    This number should be rounded to 1 decimal place"""
    return round(float(pages/40), 1)


def add_book(library=[]):
    """
    Get the boook details from the user, add the book to library,
    save it to boooks.csv, and prrint a summary.
    """
    book = {}
    book["title"] = input("Book title: ").title().strip()    # get user input in title case for "Book title: "
    book["author"] = input("Author: ").title().strip()       # get user input for "Author: "
    book["pages"] = int(input("Page count: "))               # get user input as an int for "Page count: "
    book["hours"] = estimate_reading_time(book["pages"])     # call estimate_reading_time by passing in pages
    library.append(book)

    #TODO: write the book to books.csv
    # open "books.csv" in append mode using with ... as file:
    with open("books.csv", "a") as library:
        reader = csv.DictReader(library)
        writer = csv.DictWriter(library, fieldnames=["title", "author", "pages", "hours"])
    # create a variable called writer that holds a csv.DictWriter
    #     pass in the file and fieldnames=["title", "author", "pages", "hours"]
    # use writer.writerow() to write the book dictionary to the file
        writer.writerow(book)

    print("\nBook added:\n")
    print(f"""  '{book["title"]}' by {book["author"]} -- approx. {book["hours"]} hours to read""")

    return book


def view_books(library=[]):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for num in range(len(library)):
            book = library[num]
            print(f"""  {num+1}. '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} hours to read)""")


def load_books():
    """
    Read every book saved in books.csv and return them as a list of dictionaries
    """
    library = []
    # open "books.csv" using with ... as file:
    # create a variable called reader that holds csv.DictReader(file)
    # for each row in reader:
    # create a dictionary called book:
    #     "title"  -> row["title"]
    #     "author" -> row["author"]
    #     "pages"  -> row["pages"] converted with int()
    #     "hours"  -> row["hours"] converted with float()
    # append book to library

    return library



def show_menu():
    print(f'''
    What would you like to do?
    
    1) View books
    2) Add a book
    
    q) Quit
    
    ''')
    option = input("> ").strip().lower()
    return option


def main():
    library = []
    option = ''
    dashboard()
    while option != 'q':
        option = show_menu()

        match option:
            case '1':   # View books
                view_books(library)
            case '2':   # Add a book
                add_book(library)
            case 'q' | 'quit' | 'exit':
                break
            case _:
                print("Sorry, that option isn't available.")
                continue

    print("Goodbye!")


if __name__ == "__main__":
    main()
