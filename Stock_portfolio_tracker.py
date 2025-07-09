stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

total = 0

print("Welcome to the Stock Tracker!")

while True:
    stock = input("Enter stock name (or 'DONE' to finish): ").upper()
    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input(f"How many shares of {stock} do you have? "))
        total += stock_prices[stock] * qty
    else:
        print("Stock not found.")

print("\nTotal Investment: $", total)

