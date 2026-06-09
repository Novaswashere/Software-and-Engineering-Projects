book_titles = [
 "The Hobbit",
    "1984",
    "Dune",
    "Project Hail Mary",
    "Fahrenheit 451"
]

book_authors = [
    "J.R.R. Tolkien",
    "George Orwell",
    "Frank Herbert",
    "Andy Weir",
    "Ray Bradbury"
]

book_availability = [
    "Yes",
    "Not",
    "Yes",
    "Yes",
    "Not"
]


class Library():

    def __init__(self,books,authors,availibility):
        self.collection = books
        self.authors = authors
        self.availibilty = availibility

    def option1(self):
        for i in range(len(self.collection)):
            if book_availability[i].lower() == "yes":
                print(f"The Book Titled: '{self.collection[i]}' is in stock" )
            else:
                print(f"The Book Titled: '{self.collection[i]}' is not in stock")

    def option2(self,book):
        for i in range(len(self.collection)):
            if self.collection[i].lower() == book.lower() and self.availibilty[i].lower() == "yes":
                print("Book can be checked out!!, now the Book has been updated to unavailable in the data system")
                self.availibilty[i] = "Not"


    def option3(self,book):
        for i in range(len(self.collection)):
            if self.collection[i].lower() == book.lower() and self.availibilty[i].lower() == "not":
                print("Book has been returned succesfuly")
                self.availibilty[i] = "Yes"
            elif self.collection[i].lower() == book.lower() and self.availibilty[i].lower() == "yes":
                print("This book is already available")

    def option4(self):
        print("The Currently Available Books are: ")
        for i in range(len(self.collection)):
            print(f"{i+1}. {self.collection[i]}")

        integer = int(input("Please choose via an integer for book you want further details off: "))
        idx = integer - 1 #Get the index of the book details are needed off !
        if self.availibilty[idx].lower() == "not":
            print(f"The Book Titled '{self.collection[idx]}' is written by the Author '{self.authors[idx]}' and is currently not available in stock ")
        else:
            print(f"The Book Titled '{self.collection[idx]}' is written by the Author '{self.authors[idx]}' and is currently  available in stock ")




while True:
    print("------Menu------")
    print('\n')
    print("Select on of the following options to continue or enter 0 to quit the Menu")
    print('\n')
    print("1. View a complete list of all books in the system alongside their current availability.")
    print("2. Check out a specific book.")
    print("3. Return a specific book.")
    print("4. View Specific Book Details")
    print("0. Enter 0 to quit. ")
    print('\n')

    lib = Library(book_titles,book_authors,book_availability)
    option = int(input("Selection Your option: "))

    if option == 1:
        lib.option1()

    elif option == 2:
        # Ensures that the book entered exists in the librarys colection!
        found = False
        while found == False:
            bookName = input("Please enter the name of the book you want to checkout!: ")
            for book in book_titles:
                if bookName.lower() == book.lower():
                    found = True
        lib.option2(bookName)

    elif option == 3:
        found = False
        while found == False:
            bookName = input("Please enter the name of the book you want to return: ")
            for book in book_titles:
                if bookName.lower() == book.lower():
                    found = True
        lib.option3(bookName)

    elif option == 4:
        lib.option4()

    elif option == 0:
        print("Thanks for using our Digital Library System!! ")
        break

