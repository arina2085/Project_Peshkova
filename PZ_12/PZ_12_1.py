#В матрице найти суммы элементов каждого столбца и поместить их в новый массив. Выполнить замену элементов второй строки исходной матрицы на полученные суммы. 

import random

matrix = [[random.randint(0, 10) for j in range(5)] for i in range(5)]

for row in matrix:
    print(' '.join(map(str, row)))

column_sums = list(map(sum, zip(*matrix)))

print("Суммы столбцов:")
print(column_sums)

matrix[1] = column_sums

print("Матрица после замены второй строки:")
for row in matrix:
    print(' '.join(map(str, row)))
