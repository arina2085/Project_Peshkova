#Дан прямоугольник
def square():
    try:
        a = int(input("Введите длину прямоугодьника: "))
        b = int(input("Введите ширину прямоугодьника: "))
        if a <= 0:
            print("Число не может быть меньше или равно нулю")
            a = int(input("Введите длину прямоугодьника: "))
        elif b <= 0:
            print("Число не может быть меньше или равно нулю")
            b = int(input("Введите ширину прямоугодьника: "))
        
        current_a = a
        current_b = b
        count = 0

        while current_a > 0 and current_b > 0:
            side = min(current_a, current_b)
            if current_a > current_b:
                current_a -= side
            else:
                current_b -= side
            count += 1 
        print(count)
    except Exception as e:
        print("Ошибка!")

square()