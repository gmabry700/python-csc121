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
    Get the book details from the user, add the book to library,
    save it to books.csv, and print a summary.
    """
    book = {}
    book["title"] = input("Book title: ").title().strip()    # get user input in title case for "Book title: "
    book["author"] = input("Author: ").title().strip()       # get user input for "Author: "
    book["pages"] = int(input("Page count: "))               # get user input as an int for "Page count: "
    book["hours"] = estimate_reading_time(book["pages"])     # call estimate_reading_time by passing in pages
    library.append(book)

    # write the book to books.csv
    with open("books.csv", "a") as library:
        writer = csv.DictWriter(library, fieldnames=["title", "author", "pages", "hours"])
        writer.writerow(book)

    print("\nBook added:\n")
    print(f"""  '{book["title"]}' by {book["author"]} -- approx. {book["hours"]} hours to read""")

    return book


def format_book(book, num):
    return f"""{num}. '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} hours to read)"""


def view_books(library=[]):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for num in range(len(library)):
            print(format_book(library[num], num+1))

def load_books():
    """
    Read every book saved in books.csv and return them as a list of dictionaries
    """
    library = []
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            book = {
                "title": row["title"],
                "author": row["author"],
                "pages": int(row["pages"]),
                "hours": float(row["hours"])
            }
            library.append(book)
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
    library = load_books()
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
