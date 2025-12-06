#Дан список размера n. Осуществить циклический сдвиг элементов списка влево на одну позицию (при этом An перейдет в A(n-1), A(n-1) - A(n-2) ... A1 - в An)

import random

n = int(input("Введите длину списка: "))
a = [random.randint(1,n) for _ in range(n)]
print(a)

if n > 1:
    element = a.pop(0)
    a.append(element)
    
print(a)