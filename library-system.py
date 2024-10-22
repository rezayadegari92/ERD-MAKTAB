class Book:
    def __init__(self, isbn, title, author, inventory : bool):
        self.inventory = inventory
        self.isbn = isbn
        self.title = title
        self.author = author



class Member:
    def __init__(self, member_id, name, address):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.borrowed_books = []

    def borrow_book(self, book, due_date):
        borrowing_details = Borrowing(self, book, due_date)
        self.borrowed_books.append(borrowing_details)

class Library:
    def __init__(self, member, book, due_date):
        self.member = member
        self.book = book
        self.borrow_date = datetime.now()
        self.due_date = due_date