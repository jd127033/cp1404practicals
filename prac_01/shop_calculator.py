number_of_items = (int(input("Number of items: ")))
total_price = 0
if number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = (int(input("Number of items: ")))
for i in range(1, (number_of_items + 1), 1):
    item_price = (float(input("Price of item: ")))
    total_price = total_price + item_price
print(f"Total price for {number_of_items} items is ${total_price}")