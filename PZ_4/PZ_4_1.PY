#Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1 + A + A2 + A3 + ... + AN

a = input("Введите вещественное число: ")
n = input("Введите целое число (>0): ")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Ошибка! Введите число.")
        a = input("Введите вещественное число: ")

while type(n) != float:
    try:
        n = float(n)
        if n < 0:
            print("Ошибка! Введите число больше нуля.")
            n = input("Введите целое число: ")
    except ValueError:
        print("Ошибка! Введите число.")
        n = input("Введите вещественное число: ")

i = 1
while i <= n:
    i += a**n
    print(i)