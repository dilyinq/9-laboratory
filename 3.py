import csv

total_sum = 0
buy_list = []

with open(r"9.3.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for a in reader:
        product, quantity, price = a
        b = int(quantity) * int(price)
        total_sum += b
        buy_list.append(f"{product} - {quantity} шт. за {price} руб.")

print("Нужно купить:")
for item in buy_list:
    print(item)

print(f"Итоговая сумма: {total_sum} руб.")
