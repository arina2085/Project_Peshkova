#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новывй текстовый файл (.txt) следующего вида, предворительно выполнив требуемую обработку элементов: 
#Исходные данные:
#Количество элементов:
#Индекс последнего минимального элемента:
#Умножаем все элементы на первый элемент:

import random

chars = [random.randint(-10,10) for i in range(10)]

f = open("file.txt", "w", encoding="UTF-8")
f.write(" ".join(map(str, chars)))
f.close()

count = len(chars)

min_num = min(chars)
min_last = 0
for i in range(len(chars)):
    if chars[i] == min_num:
        min_last = i

num1 = chars[0]
p = []
for i in chars:
    p.append(i * num1)

f3 = open("new_file.txt", "w", encoding="UTF-8")
f3.write(f"Исходные данные: {" ".join(map(str, chars))}\n")
f3.write(f"Количество жлементов: {count}\n")
f3.write(f"Индекс последнего минимального элемента: {min_last}\n")
f3.write(f"Умножаем все элементы на первый элемент: {" ".join(map(str, p))}")
f3.close()