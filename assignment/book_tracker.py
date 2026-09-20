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
    book = {}
    book["title"] = input("Book title: ").title().strip()    # get user input in title case for "Book title: "
    book["author"] = input("Author: ").title().strip()       # get user input for "Author: "
    book["pages"] = int(input("Page count: "))               # get user input as an int for "Page count: "
    book["hours"] = estimate_reading_time(book["pages"])             # call estimate_reading_time by passing in pages
    library.append(book)

    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    print("\nBook added:\n")
    print(f"""  '{book["title"]}' by {book["author"]} -- approx. {book["hours"]} hours to read""")
    print(book)


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
    option = ''
    while option != 'q':
        dashboard()
        option = show_menu()


if __name__ == "__main__":
    main()
