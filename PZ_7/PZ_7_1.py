#Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и руских букв.

s = str(input("Введите строку: "))

count1 = 0
count2 = 0

for i in s:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        count1 += 1
    elif 'а' <= i <= 'я' or 'А' <= i <= 'Я':
        count2 += 1

result = count1 + count2
print(f"Латинских букв {count1}")
print(f"Русских букв {count2}")
print(f"Всего букв {result}")