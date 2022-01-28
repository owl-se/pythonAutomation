class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static")


class Book:
    TYPES = ("hard", "papaer")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def papaer(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight)


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()
book = Book("Potter", "hard", 1500)
print(book.name)
print(book)
book2 = Book.hardcover("Harry Potter", 1500)
print(book2)