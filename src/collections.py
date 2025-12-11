class BookCollection:
    def __init__(self, books=None):
        if books is not None:
            self._books = books
        else:
            self._books = []

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return BookCollection(self._books[index])
        else:
            return self._books[index]

    def add(self, book):
        self._books.append(book)

    def remove(self, book):
        if book in self._books:
            self._books.remove(book)
            return True
        return False

class IndexDict:
    def __init__(self):
        self._indices = {
            "author": {},
            "year": {},
            "genre": {},
            "isbn": {}
        }
    def add(self, book):
        self._indices["isbn"][book.isbn] = book

        if book.author not in self._indices["author"]:
            self._indices["author"][book.author] = []
        self._indices["author"][book.author].append(book)

        if book.year not in self._indices["year"]:
            self._indices["year"][book.year] = []
        self._indices["year"][book.year].append(book)

        if book.genre not in self._indices["genre"]:
            self._indices["genre"][book.genre] = []
        self._indices["genre"][book.genre].append(book)

    def remove_book(self, book):
        removed = False
        if book.isbn in self._indices["isbn"]:
            del self._indices["isbn"][book.isbn]
            removed = True
        if book.author in self._indices["author"]:
            if book in self._indices["author"][book.author]:
                self._indices["author"][book.author].remove(book)
                removed = True
            if not self._indices["author"][book.author]:
                del self._indices["author"][book.author]
        if book.year in self._indices["year"]:
            if book in self._indices["year"][book.year]:
                self._indices["year"][book.year].remove(book)
                removed = True
            if not self._indices["year"][book.year]:
                del self._indices["year"][book.year]
        if book.genre in self._indices["genre"]:
            if book in self._indices["genre"][book.genre]:
                self._indices["genre"][book.genre].remove(book)
                removed = True
            if not self._indices["genre"][book.genre]:
                del self._indices["genre"][book.genre]
        return removed
    def find_author(self, author):
        return self._indices["author"].get(author, [])
    def find_year(self, year):
        return self._indices["year"].get(year, [])
    def find_genre(self, genre):
        return self._indices["genre"].get(genre, [])
    def find_isbn(self, isbn):
        return self._indices["isbn"].get(isbn)
