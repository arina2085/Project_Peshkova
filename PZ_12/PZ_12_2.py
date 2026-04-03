#В матрице найти минимальный элемент в предпоследней строке.

import random

matrix = [[random.randint(0, 10) for j in range(5)] for i in range(5)]

for row in matrix:
    print(' '.join(map(str, row)))

min_element = min(matrix[-2])

print(f"Минимальный элемент: {min_element}")