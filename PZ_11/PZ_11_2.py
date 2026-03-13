#Составить генератор (yield), который выводит из строки только буквы.

import string

def letters(text):
    all_letters = string.ascii_letters + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in text:
        if i in all_letters:
            yield i

text = input()
letter = list(letters(text))
print(''.join(letter))