#Даны три целых числа: A, B, C. Проверить истинность высказывания: "Ровно одно из чисел  A, B, C положительное."

a, b, c = input("Введите первое целое число: "), input("Введите второе целое число: "), input("Введите третье целое число: ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите первое число: ")

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите первое число: ")

if a > 0 and b < 0 and c < 0:
    print("Только первое число положительное.")
elif a < 0 and b > 0 and c < 0:
    print("Тоько второе число положительное.")
elif a < 0 and b < 0 and c > 0:
    print("Только третье число положительное.")
else:
    print("Высказывания: Ровно одно из чисел  A, B, C положительное, ложно.")