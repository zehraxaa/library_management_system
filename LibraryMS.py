class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            book_title = book_info[0]
            book_author = book_info[1]
            print(f"Book: {book_title}\nAuthor: {book_author}\n")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        updated_books = []
        for line in lines:
            book_info = line.split(',')
            if book_info[0] != book_title:
                updated_books.append(line)
        self.file.seek(0)
        self.file.truncate()
        for book in updated_books:
            self.file.write(book + '\n')
        print("Book removed successfully!")


lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice =="4":
        print("Exiting the program. Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")
