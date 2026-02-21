#Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое, количество букв в нижнем регистре. Сформировать ноый файл, в который поместить текст в стихотворной форме предворителльнои заменив символы нижнего регистра на верхний.

f = open("text18-15.txt", "r", encoding="UTF-16 LE")
text = f.read()
f.close()

print("Содержимое файла: ")
print(text)

count = 0 
for i in text:
    if i.islower():
        count += 1
print(f"Количество букв в нижнем регистре: {count}")

f1 = open("new_text.txt", "w", encoding="UTF-8")
new_text = text.upper()
f1.write(new_text)
f1.close()