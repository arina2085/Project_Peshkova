#https://www.webasyst.ru/wa-data/public/updates/img/09/209/7355/7355.970.jpg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Создайте заказ")
root.geometry("600x700")

root.configure(bg="#f5f5f5")

main_frame = tk.Frame(root, bg="#f5f5f5", bd=1, relief="solid")
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

header = tk.Label(main_frame, text="Создайте заказ", bg="#006680", fg="white", font=("Arial", 14, "bold"), pady=10)
header.pack(fill="x")

def create_section(title, num):
    frame = tk.Frame(main_frame, bg="#f5f5f5", padx=15, pady=10)
    frame.pack(fill="x", pady=5)

    num_label = tk.Label(frame, text=str(num), bg="#006680", fg="white", font=("Arial", 12, "bold"), width=2, height=2, bd=1)
    num_label.grid(row=0, column=0, sticky="nw", padx=(0, 10))

    title_label = tk.Label(frame, text=title, bg="#f5f5f5", fg="#006680", font=("Arial", 12, "bold"))
    title_label.grid(row=0, column=1, sticky="w")

    return frame

sec1 = create_section("Информация о заказе", 1)

labels1 = ["Номер заказа *", "Название товара", "Количество *"]
for i, lbl in enumerate(labels1):
    tk.Label(sec1, text=lbl, bg="#f5f5f5", anchor="w").grid(row=i+1, column=0, sticky="w", pady=5)
    entry = tk.Entry(sec1, width=40)
    entry.grid(row=i+1, column=1, padx=(10, 0), pady=5)

sec2 = create_section("Контактная информация", 2)

labels2 = ["Ваше имя", "Ваш email *", "Ваш телефон *"]
for i, lbl in enumerate(labels2):
    tk.Label(sec2, text=lbl, bg="#f5f5f5", anchor="w").grid(row=i+1, column=0, sticky="w", pady=5)
    if lbl == "Ваш телефон *":
        phone_entry = tk.Entry(sec2, width=40)
        phone_entry.grid(row=i+1, column=1, padx=(10, 0), pady=5)
        hint = tk.Label(sec2, text="Формат: +7 (999) 999-99-99", bg="#f5f5f5", fg="#888", font=("Arial", 8))
        hint.grid(row=i+2, column=1, sticky="w", padx=(10, 0))
    else:
        tk.Entry(sec2, width=40).grid(row=i+1, column=1, padx=(10, 0), pady=5)

sec3 = create_section("Информация о доставке", 3)

tk.Label(sec3, text="Адрес *", bg="#f5f5f5", anchor="w").grid(row=1, column=0, sticky="w", pady=5)
tk.Text(sec3, width=40, height=3).grid(row=1, column=1, padx=(10, 0), pady=5)

tk.Label(sec3, text="Время доставки", bg="#f5f5f5", anchor="w").grid(row=2, column=0, sticky="w", pady=5)

time_frame = tk.Frame(sec3, bg="#f5f5f5")
time_frame.grid(row=2, column=1, sticky="w", padx=(10, 0), pady=5)

hours = [f"{i:02d}" for i in range(0, 24)]
minutes = [f"{i:02d}" for i in range(0, 60)]

hour_var = tk.StringVar(value="00")
min_var = tk.StringVar(value="00")

hour_combo = ttk.Combobox(time_frame, textvariable=hour_var, values=hours, width=5, state="readonly")
hour_combo.pack(side="left")

tk.Label(time_frame, text=":", bg="#f5f5f5").pack(side="left", padx=2)

min_combo = ttk.Combobox(time_frame, textvariable=min_var, values=minutes, width=5, state="readonly")
min_combo.pack(side="left")

root.mainloop()