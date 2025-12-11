import random
from src.models import Book, ReferenceBook, RareBook, generate_book
from src.collections import BookCollection
from src.library import Library

def test_book_title():
    """Создание книги"""
    book = Book("Война и мир", "Толстой", 1863, "роман", "978-123-45678-9")
    assert book.title == "Война и мир"

def test_book_author():
    """Создание книги"""
    book = Book("Война и мир", "Толстой", 1863, "роман", "978-123-45678-9")
    assert book.author == "Толстой"
    assert book.is_available()

def test_book_isbn():
    """Создание книги"""
    book = Book("Война и мир", "Толстой", 1863, "роман", "978-123-45678-9")
    assert book.isbn == "978-123-45678-9"
    assert book.is_available()

def test_book_take_and_return():
    """Взятие и возврат книги"""
    book = Book("Война и мир", "Толстой", 1863, "роман", "978-123-45678-9")
    assert book.take_book()
    assert not book.is_available()
    assert not book.take_book()
    book.return_book()
    assert book.is_available()

def test_reference_book():
    """Проверяем пособие"""
    ref_book = ReferenceBook("Пособие", "Автор", 2020, "классика", "978-111-22445-3", "художественная литература")
    assert ref_book.categoria == "художественная литература"
    assert ref_book.take_book()

def test_bookcollection():
    """Функции BookCollection"""
    collection = BookCollection()
    assert len(collection) == 0
    book = Book("Книга", "Автор", 2000, "жанр", "978-123-45678-9")
    collection.add(book)
    assert len(collection) == 1
    assert collection[0] == book
    assert collection.remove(book)
    assert len(collection) == 0
    assert not collection.remove(book)

def test_errors():
    """Обработку ошибок"""
    library = Library()
    book = Book("Книга", "Автор", 2000, "Жанр", "123")
    assert not library.remove_book(book)
    assert library.find_by_author("Неизвестный") == []
    assert library.find_by_year(9999) == []
    assert library.find_by_genre("Нет такого") == []

def test_generate_title():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert hasattr(book, 'title')

def test_generate_author():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert hasattr(book, 'author')

def test_generate_year():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert hasattr(book, 'year')

def test_generate_genre():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert hasattr(book, 'genre')

def test_generate_isbn():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert hasattr(book, 'isbn')

def test_generate_start_isbn():
    """Генерацию книги"""
    random.seed(42)
    book = generate_book()
    assert isinstance(book, (Book, ReferenceBook, RareBook))
    assert book.isbn.startswith("978-")
