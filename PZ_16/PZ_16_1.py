#Создайте класс "Книга", который имеет атрибуты название, автор и количество страниц. Добавте методы для чтения и записи книг.

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        print(f"Создана книга: {name} автора {author} с {pages} страницами")

    def get_info(self):
        return f"Название: {self.name}\n Автор: {self.author}\n Страниц: {self.pages}"

    def set_name(self, new_name):
        self.name = new_name
        print(f"Название книги изменено на: {new_name}")

    def set_author(self, new_author):
        self.author = new_author
        print(f"Автор книги изменен на: {new_author}")

    def set_pages(self, new_pages):
        if new_pages > 0:
            self.pages = new_pages
            print(f"Количество страниц изменено на: {new_pages}")
        else:
            print("Ошибка: количество страниц должно быть положительным числом!")

    def read(self):
        print(f"Читаем книгу '{self.name}'...")
        for page in range(1, self.pages + 1):
            if page % 10 == 0:
                print(f"Прочитано {page} страниц из {self.pages}")
        print(f"Книга '{self.name}' прочитана полностью!")

    def write(self, new_content):
        print(f"Добавляем содержимое в книгу '{self.name}'...")
        print(f"Добавлено новое содержимое: '{new_content}'")
        print(f"Теперь книга '{self.name}' содержит обновленный контент")


print("Создание новой книги")
name = input("Введите название книги: ")
author = input("Введите автора: ")

while True:
    try:
        pages = int(input("Введите количество страниц: "))
        if pages > 0:
            break
        else:
            print("Количество страниц должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

book = Book(name, author, pages)

print("\nИнфо о книге")
print(book.get_info())

print("\nДоп возможности")
book.read()
book.write("Новые главы")