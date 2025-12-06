#Дан спимок А размера n. Вывести его элементы в следующем порядке: A1, An, A2, A(n-1), A3, A(n-2)

import random

n = int(input("Введите размер списка: "))
a = [random.randint(1,n) for _ in range(n)]
print(a)

result = []
left = 0
right = n - 1
turn = True

while left <= right:
    if turn:
        result.append(a[left])
        left += 1
    else: 
        result.append(a[right])
        right -= 1
    turn = not turn
    
print(result)