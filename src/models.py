import random
BOOK_INFORMATION = {
    "Толстой":{
        "books":["Война и мир","Анна Каренина"],
        "genre":"Роман",
        "years":{"Война и мир": 1863, "Анна Каренина": 1873}
    },
    "Булгаков": {
        "books": ["Мастер и Маргарита", "Собачье сердце"],
        "genre": "фантастика",
        "years": {"Мастер и Маргарита": 1928, "Собачье сердце": 1925}
    },
    "Пушкин": {
        "books": ["Метель", "Барышня-крестьянка", "Выстрел"],
        "genre": "Повесть",
        "years": {"Метель": 1830,"Барышня-крестьянка": 1830, "Выстрел": 1830}
    },
    "Островский": {
        "books": ["Гроза", "Бесприданница"],
        "genre": "Драма",
        "years": {"Гроза": 1859, "Бесприданница": 1879}
    }
}

CATEGORY_INFORMATION = ["художественная литература"]
CONDITION_INFORMATION = ["хорошее", "плохое", "удовлетворительное"]
MIN_YEAR = 1830
MAX_YEAR = 1928

def generate_book():
    "Генерация случайной книги"
    author = random.choice(list(BOOK_INFORMATION.keys()))
    author_data = BOOK_INFORMATION[author]
    title = random.choice(author_data["books"])
    genre = author_data["genre"]
    year = author_data["years"][title]
    isbn = f"978-{random.randint(100,999)}-{random.randint(10000, 99999)}-{random.randint(0, 9)}"
    rand = random.randint(0,6)
    if rand <=1:
        return ReferenceBook(title, author, year, genre, isbn, random.choice(CATEGORY_INFORMATION))
    elif rand <=2:
        return RareBook(title, author, year, genre, isbn, random.choice(CONDITION_INFORMATION))
    else:
        return Book(title, author, year, genre, isbn)

class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self._is_available = True

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.year}')"
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
    def is_available(self): #доступна ли книга
        return self._is_available
    def take_book(self):
        if self._is_available: #берем книгу
            self._is_available = False #убрали с полки
            return True #успешно взяли
        return False #не получилось взять
    def return_book(self):
        self._is_available = True #вернули книгу обратно

class ReferenceBook(Book):
    "Пособие нельзя брать домой"
    def __init__(self, title, author, year, genre, isbn, categoria):
        super().__init__(title, author, year, genre, isbn)
        self.categoria = categoria
    def take_book(self): #справочник нельзя брать домой
        if self._is_available:  # берем книгу
            self._is_available = False  # убрали с полки
            return True  # успешно взяли
        return False  # не получилось взять
    def __str__(self):
        return f"{super().__str__()} Пособие: {self.categoria}"

class RareBook(Book):
    "Редкие книги выдаются с ограничениями в количестве"
    def __init__(self, title, author, year, genre, isbn, condition):
        super().__init__(title, author, year, genre, isbn)
        self.condition = condition
        self.take_count = 0
    def take_book(self):
        if self.take_count<5 and self._is_available: #можно брать только 4 рааа редкую книгу
            self._is_available = False
            self.take_count += 1
            return True
        return False
    def __str__(self):
        return f"{super().__str__()} Книга редкая в {self.condition} состоянии и выдавалась {self.take_count} раз"
