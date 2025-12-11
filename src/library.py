from src.collections import BookCollection, IndexDict
class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()

    def add_book(self, book):
        self.books.add(book)
        self.index.add(book)
        return True
    def remove_book(self, book):
        if self.books.remove(book):
            self.index.remove_book(book)
            return True
        return False

    def remove_random_book(self, book):
        if len(self.books)>0:
            import random
            book = random.choice(self.books)
            self.books.remove(book)
            return book
        return None

    def find_by_author(self, author):
        return self.index.find_author(author)

    def find_by_year(self, year):
        return self.index.find_year(year)

    def find_by_genre(self, genre):
        return self.index.find_genre(genre)

    def find_by_isbn(self, isbn):
        return self.index.find_isbn(isbn)

    def search_contains(self, text):
        results = BookCollection()
        for book in self.books:
            if text in book:
                results.add(book)
        return results

    def rebuild_index(self):
        self.index = IndexDict()
        for book in self.books:
            self.index.add(book)
