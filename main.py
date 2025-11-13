from library_books import library_books
from datetime import datetime, timedelta, date

# -------- Level 1 --------
def ViewBooks():
    print("Here are the books we currently have.")
    for book in library_books:
        if book["available"] is True:
            print(f"Id: {book['id']}, Title: {book['title']}, by: {book['author']}")
        else:
            pass

# -------- Level 2 --------
def SearchGenre():
    NoMatchingBook = True
    choice1 = input("Hello type the name of an author or genre to find books: ").lower().strip()
    print("Here are the books we have that match the search:")
    for book in library_books:
        if choice1 in book["genre"].lower() or choice1 in book["author"].lower():
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, ID: {book['id']}")
            NoMatchingBook = False
    if NoMatchingBook is True:
        print("None")

# -------- Level 3 --------
def CheckoutBook():
    WantToCheckout = input("Do you want to checkout a book, type yes or no: ").lower().strip()
    if WantToCheckout == "yes":
        SearchGenre()
        BookID = input("Type the Id of your book and I will check if it is in stock: ").strip()
        for book in library_books:
            if BookID == book['id']:  
                if book["available"] is True:
                    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {book['available']}")
                    WantToCheckout2 = input("This book is available, would you like to check it out? (yes/no): ").lower().strip()
                    if WantToCheckout2 == "yes":
                        book["available"] = False
                        current_date = date.today()
                        due_date = current_date + timedelta(days=14)
                        book["due_date"] = due_date.isoformat()               
                        book["checkouts"] = book.get("checkouts", 0) + 1      
                        print(f"The current date today is {current_date.isoformat()}")
                        print(f"The due date for '{book['title']}' is {due_date.isoformat()}")
                    else:
                        print("Ok you have decided to not check out this book.")
                else:
                    print("This book is not available")
                break
        else:
            print("No book found with that ID.")

# -------- Level 4 --------
def ReturnBook():
    print("Hello and welcome to the return")
    print("Here are the books we have. Please type the Id of the book you are returning.")
    for book in library_books:
        print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']}")
    BookGR = input("What Book are you returning today? Type the ID: ").strip()  # Book Getting Returned
    for book in library_books:
        if BookGR == book["id"]:  # exact match
            BookRID = input(f"Is this the book you would like to return? "
                            f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']} (yes/no): ").lower().strip()
            if BookRID == 'yes':
                book["due_date"] = None
                book['available'] = True
                
                print(f"Thank you for returning '{book['title']}'. The due date has been cleared.")
            else:
                print("Return cancelled.")
            break
    else:
        print("No book found with that ID.")


def OB():  # OB = overdue books
    print(f"Today's date is {date.today().isoformat()}")
    print("Due Books:")
    found = False
    for book in library_books:
        dd = book.get("due_date")
        if dd is None or book.get("available", True) is True:
            continue  # only considers checked-out items with a due_date
        try:
            duedate = datetime.strptime(dd, "%Y-%m-%d").date()
        except ValueError:
            
            continue
        if duedate < date.today():
            found = True
            days = (date.today() - duedate).days
            print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']}  ({days} day(s) overdue)")
    if found:
        ReturnOverdue = input("Would you like to return a book that's overdue? (yes/no): ").lower().strip()
        if ReturnOverdue == "yes":
            ReturnBook()
    else:
        print("No overdue books today.")

# -------- Level 5 --------
class Book:  # This is the class it's called Book and it calls all our functions
    def __init__(self):
        self.library_books = library_books

    def ViewBooks(self):
        print("Here are the books we currently have.")
        for book in self.library_books:
            if book["available"] is True:
                print(f"Id: {book['id']}, Title: {book['title']}, by: {book['author']}")
        else:
            pass

    def SearchGenre(self):  
        NoMatchingBook = True
        choice1 = input("Hello type the name of an author or genre to find books: ").lower().strip()
        print("Here are the books we have that match the search:")
        for book in self.library_books:
            if choice1 in book["genre"].lower() or choice1 in book["author"].lower():
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, ID: {book['id']}")
                NoMatchingBook = False
        if NoMatchingBook is True:
            print("None")

    def CheckoutBook(self):  
        WantToCheckout = input("Do you want to checkout a book, type yes or no: ").lower().strip()
        if WantToCheckout == "yes":
            self.SearchGenre()
            BookID = input("Type the Id of your book and I will check if it is in stock: ").strip()
            for book in self.library_books:
                if BookID == book['id']:  
                    if book["available"] is True:
                        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {book['available']}")
                        WantToCheckout2 = input("This book is available, would you like to check it out? (yes/no): ").lower().strip()
                        if WantToCheckout2 == "yes":
                            book["available"] = False
                            current_date = date.today()
                            due_date = current_date + timedelta(days=14)
                            book["due_date"] = due_date.isoformat()
                            book["checkouts"] = book.get("checkouts", 0) + 1
                            print(f"The current date today is {current_date.isoformat()}")
                            print(f"The due date for '{book['title']}' is {due_date.isoformat()}")
                        else:
                            print("Ok you have decided to not check out this book.")
                    else:
                        print("This book is not available")
                    break
            else:
                print("No book found with that ID.")

    def ReturnBook(self):  
        print("Hello and welcome to the return")
        print("Here are the books we have please type the Id of the book you are returning.")
        for book in self.library_books:
            print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']}")
        BookGR = input("What Book are you returning today type the ID: ").strip()
        for book in self.library_books:
            if BookGR == book["id"]:
                BookRID = input(
                    f"Is, Title: {book['title']}, Author: {book['author']}, ID: {book['id']}, the book you would like to return? (yes/no): "
                ).lower().strip()
                if BookRID == 'yes':
                    book["due_date"] = None
                    book['available'] = True
                    
                    print(f"Thank you for returning, Title: {book['title']}, Author: {book['author']}, ID: {book['id']} — the due date has been cleared.")
                else:
                    print("Return cancelled.")
                break
        else:
            print("No book found with that ID.")

    def OB(self): 
        print(f"Today's date is {date.today().isoformat()}")
        print("Due Books:")
        found = False
        for book in self.library_books:
            dd = book.get("due_date")
            if dd is None or book.get("available", True) is True:
                continue
            try:
                duedate = datetime.strptime(dd, "%Y-%m-%d").date()
            except ValueError:
                continue
            if duedate < date.today():
                found = True
                days = (date.today() - duedate).days
                print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']}  ({days} day(s) overdue)")
        if found:
            ReturnOverdue = input("Would you like to return a book that's overdue? (yes/no): ").lower().strip()
            if ReturnOverdue == "yes":
                self.ReturnBook()
        else:
            print("No overdue books today.")

    def AddBook(self):
        print("Add a New Book")
        book_id = input("Enter book ID(start with a capital C then any base 10 number): ").strip()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        genre = input("Enter genre: ").strip()
        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "genre": genre,
            "available": True,
            "due_date": None,
            "checkouts": 0
        }
        self.library_books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def menu(self):  
        while True:
            print("Library Menu")
            print("1) View available books")
            print("2) Search by author/genre")
            print("3) Checkout a book")
            print("4) Return a book")
            print("5) List overdue books")
            print("6) Add a book to the library")
            print("0) Quit")

            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.ViewBooks()
            elif choice == "2":
                self.SearchGenre()
            elif choice == "3":
                self.CheckoutBook()
            elif choice == "4":
                self.ReturnBook()
            elif choice == "5":
                self.OB()
            elif choice == "6":
                self.AddBook()
            elif choice in ("0",):
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
            print("__________________________")
            input("Press Enter to continue")

if __name__ == "__main__":
    # You can use this space to test your functions
    # ViewBooks()
    # SearchGenre()
    # CheckoutBook()
    # ReturnBook()
    # OB()
    b = Book()  # This allows us to call the code
    b.menu()    # Calling the code
