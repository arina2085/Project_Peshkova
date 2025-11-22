#Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.
def print_symbols():
    try:
        n = int(input("Введите количество символов: "))
        symbol = input("Введите символ для вывода: ")
        
        if n < 0:
            print("Количество символов не может быть отрицательным")
            return
        
        result = symbol * n
        print(result)
        
    except ValueError:
        print("Введите целое число")

print_symbols()