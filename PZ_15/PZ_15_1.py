#Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автомвтизированного контроля затрат на производство продукции. БД должна содержать таблицу Расходы со следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3 as sq
from datetime import datetime

with sq.connect('expenses_products.db') as con:
    cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
            kod INT PRIMARY KEY AUTOINCREMENT,
            date INT NOT NULL,
            name TEXT NOT NULL,
            expenses INT NOT NULL,
            amount INT NOT NULL
            )""")

con.commit()


def add_expense():
    """Добавить новую запись о расходах"""
    print("\n--- Добавление расходов ---")
    дата = input("Введите дату (ГГГГ-ММ-ДД): ") or datetime.now().strftime("%Y-%m-%d")
    код = input("Код продукта: ")
    наименование = input("Наименование продукта: ")
    тип_расходов = input("Тип расходов (материалы, зарплата, аренда и т.д.): ")
    
    try:
        сумма = float(input("Сумма расходов: "))
    except ValueError:
        print("Ошибка: сумма должна быть числом!")
        return

    cur.execute('''
        INSERT INTO Расходы (Дата, Код_продукта, Наименование_продукта, Расходы, Сумма)
        VALUES (?, ?, ?, ?, ?)
    ''', (дата, код, наименование, тип_расходов, сумма))
    
    con.commit()
    print("Запись успешно добавлена!")

def show_all_expenses():
    """Показать все записи"""
    print("\n--- Все расходы ---")
    cur.execute("SELECT * FROM Расходы ORDER BY Дата")
    rows = cur.fetchall()
    
    if not rows:
        print("Нет записей.")
        return

    print(f"{'Дата':<12} {'Код':<10} {'Продукт':<25} {'Расходы':<15} {'Сумма':>10}")
    print("-" * 70)
    for row in rows:
        print(f"{row[1]:<12} {row[2]:<10} {row[3]:<25} {row[4]:<15} {row[5]:>10.2f}")

def show_total():
    """Показать общую сумму расходов"""
    cur.execute("SELECT SUM(Сумма) FROM Расходы")
    total = cur.fetchone()[0]
    if total is None:
        total = 0
    print(f"\nОбщая сумма расходов: {total:.2f} руб.")

def main_menu():
    """Главное меню приложения"""
    while True:
        print("\n" + "="*40)
        print("   ПРИЛОЖЕНИЕ: РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ")
        print("="*40)
        print("1. Добавить расходы")
        print("2. Показать все расходы")
        print("3. Показать общую сумму")
        print("0. Выход")
        
        choice = input("\nВыберите действие: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_all_expenses()
        elif choice == '3':
            show_total()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
    con.close()