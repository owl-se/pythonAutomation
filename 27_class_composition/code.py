class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookSheld with {len(self.books)} books"





class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("harry potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)