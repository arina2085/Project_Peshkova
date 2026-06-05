#Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автомвтизированного контроля затрат на производство продукции. БД должна содержать таблицу Расходы со следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3

con = sqlite3.connect('expenses_products.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        product_code TEXT NOT NULL,
        product_name TEXT NOT NULL,
        expense_type TEXT NOT NULL,
        amount REAL NOT NULL
    )
""")
con.commit()

def add_expense():
    print("\nДобавление расходов")
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    code = input("Код продукта: ")
    name = input("Наименование продукта: ")
    expense_type = input("Тип расходов (материалы, зарплата, аренда и т.д.): ")
    
    try:
        amount = float(input("Сумма расходов: "))
    except ValueError:
        print("Ошибка: сумма должна быть числом!")
        return

    cur.execute('''
        INSERT INTO expenses (date, product_code, product_name, expense_type, amount)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, code, name, expense_type, amount))

    con.commit()
    print("Запись успешно добавлена!")

def show_all_expenses():
    print("\nВсе расходы")
    cur.execute("SELECT * FROM expenses ORDER BY date")
    rows = cur.fetchall()
    
    if not rows:
        print("Нет записей.")
        return

    print(f"{'Дата':<12} {'Код':<10} {'Продукт':<25} {'Расходы':<15} {'Сумма':>10}")
    print("-" * 70)
    for row in rows:
        print(f"{row[1]:<12} {row[2]:<10} {row[3]:<25} {row[4]:<15} {row[5]:>10.2f}")

def show_total():
    cur.execute("SELECT SUM(amount) FROM expenses")
    total = cur.fetchone()[0]
    if total is None:
        total = 0
    print(f"\nОбщая сумма расходов: {total:.2f} руб.")

def main_menu():
    while True:
        print("   ПРИЛОЖЕНИЕ: РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ")
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