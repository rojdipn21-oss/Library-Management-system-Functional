"""
Library management system 
(register, login) --> user
(add book, issue book, return book, view book, search book)
"""

### Creating two file named users.txt and books.txt to store user information and books information permanently inside the file

import os

if not os.path.exists('users.txt'):
    with open('users.txt', 'w') as f:
        pass
if not os.path.exists('books.txt'):
    with open('books.txt', 'w') as f:
        pass

### load data from the file
def load_user():
    """Load all the users from user.txt into dictionary"""
    users_dict = {}

    try:
        with open('users.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(',')
                    users_dict[username] = password
    except FileNotFoundError:
        print("File not found!")
    
    return users_dict

# book_id,title,author,quantity

def load_books():
    books_list = []
    try:
        with open("books.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id, title, author, quantity = line.split()

                    book = {
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    books_list.append(book)

    except FileNotFoundError:
        print("file not found!")
    return books_list

                    
def get_existing_books_id(books_list):
    """Create a set to store all the ids of the books"""
    book_ids = set()
    for book in books_list:
        # dictionary
        book_ids.add(book['id'])
    return book_ids

#### User registration
def register_user(users_dict):
    """Register a new user"""
    print("\n---- Register a New user ----")
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    if username in users_dict:
        print(f"username alrealy exists!")
        return False
    if not username or not password:
        print("Username and password cannot be empty")
        return False
    users_dict[username] = password

    # save the registered user to the file 'users.txt'
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

    print("registration successfull!")
    return True

#users_dict = load_user()
#print(users_dict)
#register_user(users_dict)

def login_user(users_dict):
    print("\n ----- Login User -----")
    username = input("Enter username ").strip()
    password = input("Enter password ").strip()

    if username in users_dict and users_dict[username] == password:
        print(f"Welcome! {username.capitalize()}")
        return username
    else:
        print("Invalid Username or password!")
        return None
    
#login_user(users_dict)


### Now books operation start
# Main menu function
def main_menu():
    """Display main menu options"""
    print("="*55)
    print("\n  Library Management System")
    print("="*55)
    print("1. Add book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Log Out")
    print("="*55)

#main_menu()


# add book
def add_book(books_list, books_ids):
    """Add a new book to the library"""
    print("\n ---- Add New Book ----")
    book_id = input("Enter the Book ID: ").strip()

    if book_id in books_ids:
        print("Book id already exists!")
        return
    
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    quantity = int(input("Enter the quantity: ").strip())

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }

    books_list.append(new_book)
    books_ids.add(book_id)

    with open('books.txt', 'a') as f:
        f.write(f"{book_id},{title},{author},{quantity} \n")
        print("Book added successfully")

books_list = load_books()
book_ids = get_existing_books_id(books_list)
print(books_list)
add_book(books_list, book_ids)

### Function to view all the books in the library
def view_books(books_list):
    """Display all the books in the library"""
    print("\n ---- All book in library ---- ")
    if not books_list:
        print("No book found in library!")
        return
    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['quantity']}")

view_books(books_list)