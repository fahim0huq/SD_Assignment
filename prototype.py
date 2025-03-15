books = [
    ("101", "bangla", "william carry"),
    ("102", "History", "sayed abu mia"),
    ("103", "Computer programming I", "henry duke")
]

def display_books():
    print("\nLibrary Collection:")
    if len(books) == 0:
        print("No books available.")
    else:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    print("-" * 40)

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    new_book = (book_id, title, author)
    books.append(new_book)
    print(f"\nBook '{title}' added successfully!")

def search_book():
    title = input("Enter Book Title to Search: ")
    for book in books:
        if book[1].lower() == title.lower():
            print(f"\nBook Found: ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
            return
    print(f"\nBook '{title}' not found in the collection.")

def main_menu():
    while True:
        print("\n--- Library System Menu ---")
        print("1. Initialize books collection")
        print("2. Add a new book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
