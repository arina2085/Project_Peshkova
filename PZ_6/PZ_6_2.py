#Дан целочисленный список размера n, все элементы которого упорядоченны (по возрастанию или по убыванию). Найти количечтво различных элементов в данном списке.

import random

n = int(input("Введите длинны списка: "))
a = [random.randint(1,n) for _ in range(n)]
a.sort(key = None)
print(a)

if n > 0:
    count = 1
    for i in range(1,n):
        if a[i] != a[i-1]:
            count += 1
            
print(count)