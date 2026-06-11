import os
os.system('clear')

# class Person:
#     #
#     number_of_people = 0

#     #Constructor
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
    
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

#     @classmethod
#     def get_number_of_people(cls):
#         return cls.number_of_people
    
# p1 = Person('Tim')
# print(Person.get_number_of_people())
# P2 = Person('Mary')
# print(Person.get_number_of_people())

class Book:
    #class attribute
    total_books = 0

    #Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.add_book()

    @classmethod
    def book_from_string(cls, book_info_string):
        book = book_info_string.split(",")
        title = book[0].strip()
        author = book[1].strip()
        return cls(title, author) # Book("1984", "George Orwell")

    @classmethod
    def add_book(cls):
        cls.total_books += 1

    @classmethod
    def get_total_count(cls):
        return f"Total books cataloged: {cls.total_books}"
    
book1 = Book("The grapes of wrath", "John Steinbeck")
# book2 = Book("1984, George Orwell")
Book.book_from_string("1984, George Orwell")

print(Book.get_total_count())