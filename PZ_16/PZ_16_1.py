#Создайте класс "Книга", который имеет атрибуты название, автор и количество страниц. Добавьте методы для чтения и записи книг.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Читаем книгу '{self.title}' автора {self.author}.")
        print(f"В книге {self.pages} страниц.")

    def write(self, text):
        print(f"Записываем в книгу '{self.title}': {text}")

book = Book("Война и мир", "Лев Толстой", 1225)

book.read()
book.write("Новая глава о судьбе героев")