#Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автомвтизированного контроля затрат на производство продукции. БД должна содержать таблицу Расходы со следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3 as sq
from data import EXPENSES_RECORDS

def init_db():
    with sq.connect("expenses.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS expenses")
        cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            product_code TEXT NOT NULL,
            product_name TEXT NOT NULL,
            expense_type TEXT NOT NULL,
            amount REAL NOT NULL
        )""")
        print("Таблица 'expenses' создана.")

def insert_data():
    with sq.connect("expenses.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expenses")
        cur.executemany(
            "INSERT INTO expenses(date, product_code, product_name, expense_type, amount) VALUES (?, ?, ?, ?, ?)",
            EXPENSES_RECORDS
        )
        print(f"Добавлено {len(EXPENSES_RECORDS)} записей.")

def show_all():
    with sq.connect("expenses.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM expenses")
        print("\nВсе записи")
        print(f"{'ID':<5} {'Дата':<12} {'Код':<8} {'Наименование':<25} {'Расходы':<15} {'Сумма':>10}")
        print("-" * 80)
        for row in cur.fetchall():
            print(f"{row[0]:<5} {row[1]:<12} {row[2]:<8} {row[3]:<25} {row[4]:<15} {row[5]:>10}")

def main():
    init_db()
    while True:
        print("\nПРИЛОЖЕНИЕ: РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ")
        print("1. Ввод данных (10 позиций)")
        print("2. Просмотр всех")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            insert_data()
        elif choice == "2":
            show_all()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    try:
        main()
    except sq.Error as e:
        print("Ошибка БД: " + str(e))
    except Exception as e:
        print("Ошибка: " + str(e))