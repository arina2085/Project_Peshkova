#Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K. Найти целое число K - показатель степени.
while True:
    n = int(input("Введите целое число: "))
    try:
        if n <= 0:
            print("Число должно быть больше нуля!")
        else:
            k = 0
            i = True
            
            while n > 1:
                if n % 2 == 0:
                    n //= 2
                    k += 1
                else:
                    i = False
                    break
            
            if i:
                print(f"Число {n} = 2^{k}")
                print(f"Показатель степени k = {k}")
                break
            else:
                print(f"Ошибка: число {n} не является степенью двойки!")
                
    except ValueError:
        print("Ошибка: введите целое число!")