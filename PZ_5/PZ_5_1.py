#Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число чисволов.
def print_symbols():
    try:
        n = int(input("Введите количество символов: "))
        symbol = input("Введите символ для вывода: ")
        
        if len(symbol) != 1:
            print("Нужно ввести ровно один символ")
            return
        
        if n < 0:
            print("Количество символов не может быть отрицательным")
            return
        
        result = symbol * n
        print(result)
        
    except ValueError:
        print("Введите целое число")

print_symbols()