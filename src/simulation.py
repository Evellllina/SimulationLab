import random
from src.library import Library
from src.models import generate_book

def run_simulation(steps: int = 10, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    library = Library()
    for _ in range(3):
        book = generate_book()
        library.add_book(book)

    events = [
        "Добавить книгу",
        "Удалить книгу",
        "Найти книгу по автору",
        "Найти книгу по году",
        "Найти книгу по жанру",
        "Взять книгу",
        "Обновить индекс",
        "Вернуть книгу"
    ]
    taken_books =[]
    for step in range(1, steps + 1):
        event = random.choice(events)

        if event == "Добавить книгу":
            new_book = generate_book()
            library.add_book(new_book)
            print(f"{step}: Добавлена книга '{new_book.title}'")

        elif event == "Удалить книгу":
            if len(library.books) >0:
                available_book = [i for i in library.books._books if i not in taken_books]
                if available_book:
                    book_to_remove = random.choice(available_book)
                    if library.remove_book(book_to_remove):
                        print(f"{step}: Удалена книга '{book_to_remove.title}'")
                    else:
                        print(f"{step}: Неудалось удалить книгу '{book_to_remove.title}'")
                else:
                    print(f"{step}: Книги заняты, удалить нельзя")
            else:
                print(f"{step}: В библиотеке нет книг")

        elif event == "Найти книгу по автору":
            if len(library.books) >0:
                book = random.choice(library.books._books)
                results = library.find_by_author(book.author)
                print(f"{step}: Поиск по автору '{book.author}' найдено {len(results)} книг")

        elif event == "Найти книгу по году":
            if len(library.books) >0:
                book = random.choice(library.books._books)
                results = library.find_by_year(book.year)
                print(f"{step}: Поиск по году '{book.year}' найдено {len(results)} книг")

        elif event == "Найти книгу по жанру":
            if len(library.books) >0:
                book = random.choice(library.books._books)
                results = library.find_by_genre(book.genre)
                print(f"{step}: Поиск по жанру '{book.genre}' найдено {len(results)} книг")

        elif event == "Взять книгу":
            if len(library.books) >0:
                available_book = [i for i in library.books._books if i not in taken_books]
                if available_book:
                    book = random.choice(available_book)
                    if book.take_book():
                        taken_books.append(book)
                        print(f"{step}: Книга '{book.title}' взяли")

        elif event == "Вернуть книгу":
            if taken_books:
                book = random.choice(taken_books)
                book.return_book()
                taken_books.remove(book)
                print(f"{step}: Книга '{book.title}' возвращена")

        elif event == "Обновить индекс":
            library.rebuild_index()
            print(f"{step}: Обновлен индекс библиотеки")

if __name__ == "__main__":
    run_simulation(steps=20, seed=777)
