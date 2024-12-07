###
from SPOT_profit import spot_profit
from Min_price import calc_min_price
###
import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook
import os
from datetime import datetime

# Функция для записи результатов в файл Excel
def save_to_excel(result_type, result_value):
    filename = 'results.xlsx'

    # Если файл не существует, создаем его и добавляем заголовки
    if not os.path.exists(filename):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Results"
        sheet.append(["Дата сделки", "Тип расчета", "Значение"])
        workbook.save(filename)

    # Открываем существующий файл и добавляем новый результат
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook["Results"]
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([current_date, result_type, result_value])
    workbook.save(filename)

def calculate_button_clicked():
    entry_price = entry_price_entry.get().split(',')
    buy_price = buy_price_buy.get().split(',')
    commission_rate = float(commission_rate_entry.get()) / 100
    exit_price = float(exit_price_entry.get())

    # Формирование списка покупок
    purchases = [(float(buy_price[i]), float(entry_price[i])) for i in range(len(entry_price))]

    # Здесь будет расчет прибыли (временно убран)
    profit = spot_profit(purchases, commission_rate, exit_price)
    messagebox.showinfo("Результат", f"Общая прибыль: ${profit}")

    # Сохраняем результат в Excel
    save_to_excel("Общая прибыль", profit)

def calculate_min_price():
    # Получение данных из полей ввода
    entry_price = entry_price_entry.get().split(',')
    buy_price = buy_price_buy.get().split(',')
    commission_rate = float(commission_rate_entry.get()) / 100

    # Проверка соответствия количества покупок и цен
    if len(entry_price) != len(buy_price):
        messagebox.showerror("Ошибка", "Количество исполненных цен и стоимости должно совпадать")
        return

    # Формирование списка покупок
    purchases = [(float(buy_price[i]), float(entry_price[i])) for i in range(len(entry_price))]

    # Расчет минимальной цены продажи
    min_price = calc_min_price(purchases, commission_rate)

    # Отображение результата
    messagebox.showinfo("Результат", f"Минимальная цена продажи для выхода в ноль: {min_price} USDT")

    # Сохраняем результат в Excel
    save_to_excel("Минимальная цена продажи", min_price)


# Создание GUI приложения
root = tk.Tk()
root.title("Калькулятор прибыли от торговли криптовалютой")

# Поля ввода
tk.Label(root, text="Исполненная цена:").grid(row=1, column=0)
entry_price_entry = tk.Entry(root)
entry_price_entry.grid(row=1, column=1)

tk.Label(root, text="Исполненная стоимость:").grid(row=2, column=0)
buy_price_buy = tk.Entry(root)
buy_price_buy.grid(row=2, column=1)

tk.Label(root, text="Комиссия (в %):").grid(row=3, column=0)
commission_rate_entry = tk.Entry(root)
commission_rate_entry.grid(row=3, column=1)

tk.Label(root, text="Цена продажи:").grid(row=4, column=0)
exit_price_entry = tk.Entry(root)
exit_price_entry.grid(row=4, column=1)

# Кнопка расчета
calculate_button = tk.Button(root, text="Минимальная цена продажи", command=calculate_min_price)
calculate_button.grid(row=5, column=0, columnspan=2)
# Кнопка расчета
calculate_button = tk.Button(root, text="Расчет", command=calculate_button_clicked)
calculate_button.grid(row=6, column=0, columnspan=2)

# Запуск приложения
root.mainloop()