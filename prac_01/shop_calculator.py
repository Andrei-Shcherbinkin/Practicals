DISCOUNT_PRICE = 0.9
total_price = 0
items_number = int(input("Enter the number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Enter the number of items: "))
for i in range(1, items_number+1):
    price = float(input(f"Price of item {i}: "))
    total_price += price
if total_price > 100:
    total_price = total_price * DISCOUNT_PRICE
print(f"Total price for 3 items is ${total_price}")