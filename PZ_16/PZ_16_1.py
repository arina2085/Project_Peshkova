#Создайте класс "Книга", который имеет атрибуты название, автор и количество страниц. Добавьте методы для чтения и записи книг.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def read(self):
        print(f"Читаем книгу '{self.title}' автора {self.author}.")
        print(f"В книге {self.pages} страниц.")

    def write(self, text):
        print(f"Записываем в книгу '{self.title}': {text}")

print("Создание книги")
title = input("Введите название книги: ")
author = input("Введите автора: ")
pages = int(input("Введите количество страниц: "))

book = Book(title, author, pages)
book.write(input("Введите новую запись: "))
print(book.get_info())