def dashboard():
    """Prints
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    # your code here
    print('=' * 40)
    print('  📚  YOUR LIBRARY')
    print('=' * 40)


def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour.
    This number should be rounded to 1 decimal place"""
    # your code here
    return round(float(pages/40), 1)


def add_book():
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    title = input("Book title: ").title().strip()    # get user input in title case for "Book title: "
    author = input("Author: ").title().strip()       # get user input for "Author: "
    pages = int(input("Page count: "))               # get user input as an int for "Page count: "
    hours = estimate_reading_time(pages)             # call estimate_reading_time by passing in pages

    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    print("\nBook added:\n")
    print(f"  '{title}' by {author} -- approx. {hours} hours to read")


def main():
    dashboard()
    add_book()


if __name__ == "__main__":
    main()
