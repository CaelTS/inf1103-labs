inventory = 0

while True:
    stock = input("\nEnter Stock Quantity: ")
    if stock.isdigit():
        break;
    elif stock == "quit":
        break;