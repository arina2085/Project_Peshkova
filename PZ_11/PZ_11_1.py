#В последовательности на n целых чисел найти и вывести: 
# 1. максимальное среди положительных 
# 2. минимальное среди отрицательных 
# 3. произведение элементов

from functools import reduce

nums = list(map(int, input("Введите числа: ").split()))
print(nums)

positive = list(filter(lambda x: x > 0, nums))
negative = list(filter(lambda x: x < 0, nums))

print(max(positive) if positive else "Нет положительных")
print(min(negative) if negative else "Нет отрицательных")
print(reduce(lambda x, y: x * y, nums))
