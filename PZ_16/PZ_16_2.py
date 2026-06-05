# Создайте класс "Животное", который содержит информацию о виде и возрасте животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса "Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, animal_type, age):
        self.animal_type = animal_type
        self.age = age

    def get_info(self):
        return f"Вид: {self.animal_type}, Возраст: {self.age} лет"

class Dog(Animal):
    def __init__(self, animal_type, age, breed):
        super().__init__(animal_type, age)
        self.breed = breed

    def get_info(self):
        return f"Вид: {self.animal_type}, Возраст: {self.age} лет, Порода: {self.breed}"

class Cat(Animal):
    def __init__(self, animal_type, age, breed):
        super().__init__(animal_type, age)
        self.breed = breed

    def get_info(self):
        return f"Вид: {self.animal_type}, Возраст: {self.age} лет, Порода: {self.breed}"

print("Создание собаки")
dog_type = input("Введите вид животного: ")
dog_age = int(input("Введите возраст: "))
dog_breed = input("Введите породу: ")

dog = Dog(dog_type, dog_age, dog_breed)
print(dog.get_info())

print("\nСоздание кошки")
cat_type = input("Введите вид животного: ")
cat_age = int(input("Введите возраст: "))
cat_breed = input("Введите породу: ")

cat = Cat(cat_type, cat_age, cat_breed)
print(cat.get_info())