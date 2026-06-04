#Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и руских букв.

import tkinter as tk
from tkinter import ttk

def count_letters():
    s = entry.get()
    count1 = 0  #латинские
    count2 = 0  #русские

    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            count1 += 1
        elif 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            count2 += 1

    result = count1 + count2
    label_result.config(
        text=f"Латинских букв: {count1}\n"
            f"Русских букв: {count2}\n"
            f"Всего букв: {result}"
    )

root = tk.Tk()
root.title("Подсчёт букв")
root.geometry("400x250")

header = tk.Label(root, text="Введите строку:", font=("Arial", 12))
header.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 10))
entry.pack(pady=5)

btn = ttk.Button(root, text="Посчитать", command=count_letters)
btn.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 11), justify="left")
label_result.pack(pady=10)

root.mainloop()