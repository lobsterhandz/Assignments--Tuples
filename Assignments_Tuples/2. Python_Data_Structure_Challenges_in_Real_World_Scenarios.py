# 2. Library System Enhancement
# Task: Update the library system by adding new books without allowing duplicates.

def add_book(library, new_book):
    if new_book not in library:
        library.append(new_book)
        return f"Book '{new_book[0]}' by {new_book[1]} added to the library."
    else:
        return f"Book '{new_book[0]}' by {new_book[1]} already exists in the library."

# System loop to get user input for library books with exception handling
library = [
    ("1984", "George Orwell"),
    ("Brave New World", "Aldous Huxley")
]

while True:
    try:
        book_title = input("Enter book title (or 'done' to finish): ").strip()
        if book_title.lower() == 'done':
            break
        if not book_title:
            print("Book title cannot be empty. Please try again.")
            continue
        author = input("Enter author: ").strip()
        if not author:
            print("Author name cannot be empty. Please try again.")
            continue
        new_book = (book_title, author)
        # Ensure case insensitive duplicate check
        if any(existing_book[0].lower() == new_book[0].lower() and existing_book[1].lower() == new_book[1].lower() for existing_book in library):
            print(f"Book '{new_book[0]}' by {new_book[1]} already exists in the library.")
        else:
            print(add_book(library, new_book))
    except Exception as e:
        print(f"An error occurred: {e}")

