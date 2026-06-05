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
            print(f"{row[0]:<5} {row[1]:<12} {row[2]:<8} {row[3]:<25} {row[4]:<15} {row[5]:>10.2f}")


def find_by_id(cur, record_id):
    cur.execute("SELECT * FROM expenses WHERE id = ?", (record_id,))
    return cur.fetchone()


def update_db():
    with sq.connect("expenses.db") as con:
        cur = con.cursor()

        try:
            record_id = int(input("Введите ID записи для редактирования: "))
        except ValueError:
            print("Ошибка: ID должен быть числом!")
            return

        row = find_by_id(cur, record_id)
        if not row:
            print(f"Запись с ID {record_id} не найдена.")
            return

        print(f"\nНайдена запись: ID={row[0]}, Дата={row[1]}, Код={row[2]}, "
            f"Наименование={row[3]}, Расходы={row[4]}, Сумма={row[5]}")

        print("\nЧто изменить?")
        print("1. Дата")
        print("2. Код продукта")
        print("3. Наименование продукта")
        print("4. Тип расходов")
        print("5. Сумма")
        field_choice = input("Выберите поле (1-5): ")

        fields = {
            "1": ("date", "Введите новую дату: "),
            "2": ("product_code", "Введите новый код продукта: "),
            "3": ("product_name", "Введите новое наименование: "),
            "4": ("expense_type", "Введите новый тип расходов: "),
            "5": ("amount", "Введите новую сумму: "),
        }

        if field_choice not in fields:
            print("Неверный выбор поля.")
            return

        column, prompt = fields[field_choice]
        new_value = input(prompt)

        if column == "amount":
            try:
                new_value = float(new_value)
            except ValueError:
                print("Ошибка: сумма должна быть числом!")
                return

        cur.execute(f"UPDATE expenses SET {column} = ? WHERE id = ?", (new_value, record_id))
        print(f"Запись с ID {record_id} успешно обновлена.")


def delete_db():
    with sq.connect("expenses.db") as con:
        cur = con.cursor()

        try:
            record_id = int(input("Введите ID записи для удаления: "))
        except ValueError:
            print("Ошибка: ID должен быть числом!")
            return

        row = find_by_id(cur, record_id)
        if not row:
            print(f"Запись с ID {record_id} не найдена.")
            return

        print(f"\nУдаляемая запись: ID={row[0]}, Дата={row[1]}, "
            f"Наименование={row[3]}, Сумма={row[5]}")

        confirm = input("Подтвердите удаление (да/нет): ")
        if confirm.lower() in ("да", "д", "yes", "y"):
            cur.execute("DELETE FROM expenses WHERE id = ?", (record_id,))
            print(f"Запись с ID {record_id} удалена.")
        else:
            print("Удаление отменено.")

def main():
    init_db()
    while True:
        print("\n=== ПРИЛОЖЕНИЕ: РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ ===")
        print("1. Ввод данных (10 позиций)")
        print("2. Просмотр всех")
        print("3. Редактирование записи")
        print("4. Удаление записи")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            insert_data()
        elif choice == "2":
            show_all()
        elif choice == "3":
            update_db()
        elif choice == "4":
            delete_db()
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