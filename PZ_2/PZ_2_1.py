number = int(input("Введите трехзначное число: "))
num1 = number//100
num2 = (number // 10) % 10
num3 = number % 10
sum = num1 + num2 + num3
mult = num1 * num2 * num3
print(f"Сумма: {sum}, произведение: {mult}")
