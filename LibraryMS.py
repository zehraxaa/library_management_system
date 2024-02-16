class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.file = open(self.filename, 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title} ,{author} ,{release_date} ,{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        print("Book removed successfully.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    user_input = input("Enter your choice (1-4): ")

    if user_input == '1':
        lib.list_books()
    elif user_input == '2':
        lib.add_book()
    elif user_input == '3':
        lib.remove_book()
    elif user_input == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
