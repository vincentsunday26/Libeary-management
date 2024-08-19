class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = False

    # Getters and Setters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and Setters
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and Setters
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Select an option: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_new_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_new_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_new_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date: ")

            new_book = Book(title, author, genre, publication_date)
            self.books.append(new_book)
            print(f"Book '{title}' added successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def borrow_book(self):
        try:
            title = input("Enter the title of the book to borrow: ")
            for book in self.books:
                if book.get_title() == title and not book.is_borrowed():
                    book.borrow()
                    print(f"You have borrowed '{title}'.")
                    return
            print(f"Book '{title}' is not available.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_book(self):
        try:
            title = input("Enter the title of the book to return: ")
            for book in self.books:
                if book.get_title() == title and book.is_borrowed():
                    book.return_book()
                    print(f"You have returned '{title}'.")
                    return
            print(f"Book '{title}' was not borrowed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_book(self):
        try:
            title = input("Enter the title of the book to search: ")
            for book in self.books:
                if book.get_title() == title:
                    print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Publication Date: {book.get_publication_date()}, Borrowed: {book.is_borrowed()}")
                    return
            print(f"Book '{title}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_all_books(self):
        try:
            if not self.books:
                print("No books available.")
            for book in self.books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Publication Date: {book.get_publication_date()}, Borrowed: {book.is_borrowed()}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_new_user(self):
        try:
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")

            new_user = User(name, library_id)
            self.users.append(new_user)
            print(f"User '{name}' added successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_user_details(self):
        try:
            library_id = input("Enter library ID: ")
            for user in self.users:
                if user.get_library_id() == library_id:
                    print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {user.get_borrowed_books()}")
                    return
            print(f"User with ID '{library_id}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_all_users(self):
        try:
            if not self.users:
                print("No users available.")
            for user in self.users:
                print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {user.get_borrowed_books()}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_new_author(self):
        try:
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")

            new_author = Author(name, biography)
            self.authors.append(new_author)
            print(f"Author '{name}' added successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_author_details(self):
        try:
            name = input("Enter author name: ")
            for author in self.authors:
                if author.get_name() == name:
                    print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
                    return
            print(f"Author '{name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_all_authors(self):
        try:
            if not self.authors:
                print("No authors available.")
            for author in self.authors:
                print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()
